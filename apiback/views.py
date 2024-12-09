from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

#Affichage de tous les évènements disponibles
class EventListAPI(APIView):
    def get(self, request):
        # Récupérer tous les événements "à venir" et "en cours"
        events = Event.objects.filter(status__in=['à venir', 'en cours']).order_by('date')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
