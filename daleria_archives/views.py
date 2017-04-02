from django.core import serializers
from django.shortcuts import render
from daleria_archives.models import Card
from django.http import HttpResponseNotFound

def validate_custom_list_request(request):
    """
    validates whether a request for a custom card list is valid
    """

    if request.method != 'POST':
        return False
    try:
        request.POST['request_set']
    except KeyError:
        return False

    return True

def full_list_page(request):
    """
    returns full menu of all game cards
    """
    cards = serializers.serialize("json",Card.objects.all())
    return render(request, 'serve-json.html', {'data': cards})

def request_list_page(request):
    """
    returns data for sub-set of requested cards
    """

    if validate_custom_list_request(request):
        return render(request, 'serve-json.html', {'data': 'blarg'})

    else:
        return HttpResponseNotFound('data not found')

def home_page(request):
    return render(request, 'home.html')
