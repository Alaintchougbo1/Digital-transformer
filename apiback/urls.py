from django.contrib import admin
from django.urls import path
from .views import EventListAPI
from .views import NotificationList

urlpatterns = [
    path('api/events/', EventListAPI.as_view(), name='event_list_api'),
]

urlpatterns = [
    path('api/notifications/', NotificationList.as_view(), name='notification_list_api'),
]