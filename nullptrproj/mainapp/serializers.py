from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(
        source='like_set.count', 
        read_only=True
    )
    class Meta:
        model = models.Project
        fields = ['name', 'video_profile', 'video_description', 'description', 'like_count']

class MatchSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = models.Match
        fields = ['investor', 'project', 'hasEnded']