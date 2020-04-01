from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Counter


# Create your views here.
def index(request):
    counter = Counter.objects.first()
    context = {'counter': counter}
    return render(request, 'counter/index.html', context)


def increment(request):
    counter = Counter.objects.first()
    counter.increment()
    counter.save()
    return HttpResponseRedirect(reverse('counter:index'))


def decrement(request):
    counter = Counter.objects.first()
    counter.decrement()
    counter.save()
    return HttpResponseRedirect(reverse('counter:index'))


def set_value(request):
    print(request.POST['value'])
    print(request.POST)
    counter = Counter.objects.first()
    counter.value = request.POST['value']
    counter.save()
    return HttpResponseRedirect(reverse('counter:index'))
