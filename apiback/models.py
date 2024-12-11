# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

### CUSTOM USER MODEL ###
class User(AbstractUser):
    ROLE_CHOICES = (
        ('viewer', 'Viewer'),
        ('streamer', 'Streamer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')

    def __str__(self):
        return self.username



# Validator for image files
def validate_image_file(file):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported image format. Allowed formats are: {', '.join(valid_extensions)}")

# Validator for video files
def validate_video_file(file):
    valid_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported video format. Allowed formats are: {', '.join(valid_extensions)}")

class Event(models.Model):
    # Event details
    title = models.CharField(max_length=200)
    description = models.TextField()
    streamer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')

    # Pricing and access
    is_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Media
    video_file = models.FileField(upload_to='videos/', null=True, blank=True, validators=[validate_video_file])
    video_url = models.URLField(null=True, blank=True)  # External video URL
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True, validators=[validate_image_file])

    # Timing
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        # Ensure price is provided if the event is paid
        if self.is_paid and (self.price is None or self.price <= 0):
            raise ValidationError("Paid events must have a valid price.")
        # Ensure either video_file or video_url is provided, not both
        if self.video_file and self.video_url:
            raise ValidationError("You can only provide a video file or a video URL, not both.")

### TICKET MODEL ###
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional for anonymous users
    anonymous_name = models.CharField(max_length=50, null=True, blank=True)  # For anonymous users
    ticket_code = models.CharField(max_length=20, unique=True, editable=False)
    is_used = models.BooleanField(default=False)  # Indicates if the ticket was used to access the event
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.ticket_code:
            self.ticket_code = get_random_string(length=20)  # Generate a unique ticket code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.ticket_code} for {self.event.title}"


### COMMENT MODEL ###
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional for logged-in users
    anonymous_name = models.CharField(max_length=50, null=True, blank=True)  # For anonymous users
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')  # Event (live or video)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.anonymous_name or self.user.username} on {self.event.title}"


### LIKE MODEL ###
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional for logged-in users
    anonymous_name = models.CharField(max_length=50, null=True, blank=True)  # For anonymous users
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')  # Event (live or video)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user', 'anonymous_name')  # Prevent duplicate likes

    def __str__(self):
        return f"Like by {self.anonymous_name or self.user.username} on {self.event.title}"

class EventAccess(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='access_list')  # Event linked
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional for anonymous users
    anonymous_name = models.CharField(max_length=50, null=True, blank=True)  # For anonymous access
    has_access = models.BooleanField(default=False)  # Indicates if the user has access
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Access for {self.anonymous_name or self.user.username} to {self.event.title}"