from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', lambda request: render(request, 'index.html'), name='home'),
    path('events/', lambda request: render(request, 'events.html'), name='events'),
    path('about/', lambda request: render(request, 'about.html'), name='about'),
]

