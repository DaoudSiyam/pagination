import base.models
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = base.models.Video
        fields = '__all__'