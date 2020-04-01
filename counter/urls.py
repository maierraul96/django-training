from django.urls import path

from . import views

app_name = 'counter'
urlpatterns = [
    path('/increment', views.increment, name='increment'),
    path('/decrement', views.decrement, name='decrement'),
    path('', views.index, name='index')
]
