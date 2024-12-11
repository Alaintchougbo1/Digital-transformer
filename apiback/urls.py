from django.urls import path
from .views import CreateEventView, UpdateEventView, DeleteEventView, EventListView

urlpatterns = [
    path('events/create/', CreateEventView.as_view(), name='create_event'),
    path('events/<int:event_id>/update/', UpdateEventView.as_view(), name='update_event'),
    path('events/<int:event_id>/delete/', DeleteEventView.as_view(), name='delete_event'),
    path('events/', EventListView.as_view(), name='list_events'),
]

