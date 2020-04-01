from django.urls import path

from . import views

app_name = 'counter'
urlpatterns = [
    path('increment', views.increment, name='increment'),
    path('decrement', views.decrement, name='decrement'),
    path('value', views.set_value, name='set_value'),
    path('', views.index, name='index')
]
