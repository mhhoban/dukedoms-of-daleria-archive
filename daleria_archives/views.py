from django.core import serializers
from django.shortcuts import render
from daleria_archives.models import Card
from django.http import HttpResponseNotFound
import json

def validate_custom_list_request(request):
    """
    validates whether a request for a custom card list is valid
    """

    if request.method != 'POST':
        return False

    return True

def fetch_custom_list(request_set):
    """
    fetches custom list items from db
    """

    card_list = [Card.objects.get(pk=card) for card in request_set]

    return serializers.serialize('json',card_list)

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
        request_contents = json.loads(request.body)
        card_list = fetch_custom_list(request_contents['request_set'])
        return render(request, 'serve-json.html', {'data': card_list})

    else:
        return HttpResponseNotFound('data not found')

def home_page(request):
    return render(request, 'home.html')
