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
