from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    ROLES = [
        ('spectateur', 'Spectateur'),
        ('organisateur', 'Organisateur'),
        ('administrateur', 'Administrateur')
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES, default='spectateur')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    STATUS = [
        ('à venir', 'À venir'),
        ('en cours', 'En cours'),
        ('terminé', 'Terminé')
    ]

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    duration = models.IntegerField(help_text='Durée de l\'événement en minutes')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS, default='à venir')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    purchase_date = models.DateTimeField(auto_now_add=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    qr_code = models.CharField(max_length=255)

    def __str__(self):
        return f'Ticket for {self.event.title} by {self.user.name}'


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Celtiis Cash', 'Celtiis Cash'),
        ('Moov Money', 'Moov Money'),
        ('Carte Bancaire', 'Carte Bancaire')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=20, default='en attente')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.name}'

#Système de notifications
class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('new_event', 'Nouveau Evènement'),
        ('payment_due','Date limite de paiement'),
        ('event_start', 'Début d\'évènement'),
        ('invoice_received','Facture reçue'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)  # Pour gérer les dates limites de paiement

    def __str__(self):
        return f"Notification pour {self.user.username}: {self.message}"

    def mark_as_read(self):
        self.is_read = True
        self.save()
    