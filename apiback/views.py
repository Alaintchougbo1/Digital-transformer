from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Event
from .serializers import EventSerializer

class CreateEventView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users
    parser_classes = [MultiPartParser, FormParser]  # To handle file uploads

    def post(self, request):
        if request.user.role != 'streamer':
            return Response({"error": "Only streamers can create events."}, status=403)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(streamer=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UpdateEventView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id, streamer=request.user)
        except Event.DoesNotExist:
            return Response({"error": "Event not found or you do not own this event."}, status=404)

        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class DeleteEventView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id, streamer=request.user)
            event.delete()
            return Response({"message": "Event deleted successfully."}, status=200)
        except Event.DoesNotExist:
            return Response({"error": "Event not found or you do not own this event."}, status=404)

# # Create your views here

# #Affichage de tous les évènements disponibles
# class EventListAPI(APIView):
#     def get(self, request):
#         # Récupérer tous les événements "à venir" et "en cours"
#         events = Event.objects.filter(status__in=['A venir', 'En cours']).order_by('date')
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)


# #Notification de Création d'un nouvel événement    
# def create_event(request):
#     # Logique pour créer un événement...
#     new_event = Event.objects.create(...)

#     # Créer une notification pour chaque spectateur
#     users = User.objects.all()  # ou des utilisateurs spécifiques intéressés par l'événement
#     for user in users:
#         Notification.objects.create(
#             user=user,
#             message=f"Un nouvel événement '{new_event.title}' a été ajouté !",
#             notification_type='new_event'
#         )
    
#     return redirect('event_list')

# #Notification de la date limite de paiement approchante
# @shared_task
# def notify_payment_due():
#     tickets = Ticket.objects.filter(payment_due_date__lte=timezone.now() + timezone.timedelta(days=1))
    
#     for ticket in tickets:
#         Notification.objects.create(
#             user=ticket.user,
#             message=f"La date limite de paiement pour l'événement '{ticket.event.title}' approche à grands pas !",
#             notification_type='payment_due',
#             due_date=ticket.payment_due_date
#         )

# #Notification du démarrage de l'événement
# @shared_task
# def notify_event_start():
#     events = Event.objects.filter(date__lte=timezone.now() + timezone.timedelta(hours=1))  # 1 heure avant le début
#     for event in events:
#         tickets = event.ticket_set.all()
#         for ticket in tickets:
#             Notification.objects.create(
#                 user=ticket.user,
#                 message=f"L'événement '{event.title}' pour lequel vous avez acheté un billet commence bientôt !",
#                 notification_type='event_start',
#             )

# #Notification de la réception de la facture
# def process_payment(request):
#     # Logique pour traiter le paiement...
#     payment = Payment.objects.create(...)

#     # Créer une notification pour l'utilisateur après paiement
#     Notification.objects.create(
#         user=payment.user,
#         message=f"Votre facture pour l'événement '{payment.ticket.event.title}' est maintenant disponible.",
#         notification_type='invoice_received'
#     )

#     return redirect('payment_success')

# #Vue pour lister les notifications dans views.py
# class NotificationList(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         notifications = Notification.objects.filter(user=request.user)
#         serializer = NotificationSerializer(notifications, many=True)
#         return Response(serializer.data)