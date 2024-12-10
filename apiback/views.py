from django.shortcuts import redirect, render
from django.db import models
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from .models import Ticket, Notification
from celery import shared_task
from .models import Payment, Notification
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here

#Affichage de tous les évènements disponibles
class EventListAPI(APIView):
    def get(self, request):
        # Récupérer tous les événements "à venir" et "en cours"
        events = Event.objects.filter(status__in=['à venir', 'en cours']).order_by('date')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


#Notification de Création d'un nouvel événement    
def create_event(request):
    # Logique pour créer un événement...
    new_event = Event.objects.create(...)

    # Créer une notification pour chaque spectateur
    users = User.objects.all()  # ou des utilisateurs spécifiques intéressés par l'événement
    for user in users:
        Notification.objects.create(
            user=user,
            message=f"Un nouveau événement '{new_event.title}' a été ajouté !",
            notification_type='new_event'
        )
    
    return redirect('event_list')

#Notification de la date limite de paiement approchante
@shared_task
def notify_payment_due():
    tickets = Ticket.objects.filter(payment_due_date__lte=timezone.now() + timezone.timedelta(days=1))
    
    for ticket in tickets:
        Notification.objects.create(
            user=ticket.user,
            message=f"La date limite de paiement pour l'événement '{ticket.event.title}' approche !",
            notification_type='payment_due',
            due_date=ticket.payment_due_date
        )

#Notification du démarrage de l'événement
@shared_task
def notify_event_start():
    events = Event.objects.filter(date__lte=timezone.now() + timezone.timedelta(hours=1))  # 1 heure avant le début
    for event in events:
        tickets = event.ticket_set.all()
        for ticket in tickets:
            Notification.objects.create(
                user=ticket.user,
                message=f"L'événement '{event.title}' pour lequel vous avez acheté un billet commence bientôt !",
                notification_type='event_start',
            )

#Notification de la réception de la facture
def process_payment(request):
    # Logique pour traiter le paiement...
    payment = Payment.objects.create(...)

    # Créer une notification pour l'utilisateur après paiement
    Notification.objects.create(
        user=payment.user,
        message=f"Votre facture pour l'événement '{payment.ticket.event.title}' est maintenant disponible.",
        notification_type='invoice_received'
    )

    return redirect('payment_success')

#Vue pour lister les notifications dans views.py
class NotificationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)