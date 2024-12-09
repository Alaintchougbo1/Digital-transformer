from django.contrib import admin
from django.urls import path
from .views import EventListAPI

urlpatterns = [
    path('api/events/', EventListAPI.as_view(), name='event_list_api'),
]