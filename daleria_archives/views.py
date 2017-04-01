from django.core import serializers
from django.shortcuts import render
from daleria_archives.models import Card

def home_page(request):
    cards = serializers.serialize("json",Card.objects.all())

    return render(request, 'home.html', {'cards': cards})
