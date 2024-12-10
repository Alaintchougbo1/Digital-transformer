from django.contrib import admin
from django.urls import path
from .views import EventListAPI
from .views import NotificationList

urlpatterns = [
    path('events/', EventListAPI.as_view(), name='event_list_api'), # URL pour la liste des événements
    path('notifications/', NotificationList.as_view(), name='notification_list_api'),  # URL pour les notifications
]
