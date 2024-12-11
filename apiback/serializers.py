from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import Event
from .models import Notification

class EventSerializer(serializers.ModelSerializer):
    streamer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'streamer', 'is_paid', 'price', 
            'video_file', 'video_url', 'thumbnail', 
            'start_time', 'end_time', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'streamer']

    def validate(self, data):
        # Validate price for paid events
        if data.get('is_paid') and (data.get('price') is None or data.get('price') <= 0):
            raise serializers.ValidationError("Paid events must have a valid price.")
        # Ensure only one of video_file or video_url is provided
        if data.get('video_file') and data.get('video_url'):
            raise serializers.ValidationError("You can only provide a video file or a video URL, not both.")
        return data
    
class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
# class EventSerializer(serializers.ModelSerializer):
#     streamer = serializers.StringRelatedField(read_only=True)  # Show streamer username

#     class Meta:
#         model = Event
#         fields = [
#             'id', 'title', 'description', 'streamer', 'is_paid', 'price', 
#             'video_file', 'video_url', 'start_time', 'end_time', 'created_at', 'updated_at'
#         ]
#         read_only_fields = ['created_at', 'updated_at', 'streamer']

#     def validate(self, data):
#         # Ensure either a video file or video URL is provided, not both
#         if data.get('video_file') and data.get('video_url'):
#             raise serializers.ValidationError("You can only provide a video file or a video URL, not both.")
#         return data

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = ['id', 'message', 'notification_type', 'is_read', 'created_at', 'due_date']
