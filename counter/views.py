from django.shortcuts import render
from django.http import HttpResponse

from .models import Counter

# Create your views here.
def index(request):
    return HttpResponse(Counter.objects.first())
