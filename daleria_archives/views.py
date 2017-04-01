from django.core import serializers
from django.shortcuts import render
from daleria_archives.models import Card

def full_list(request):
    cards = serializers.serialize("json",Card.objects.all())

    return render(request, 'full-list.html', {'cards': cards})


def home_page(request):
    return render(request, 'home.html')
