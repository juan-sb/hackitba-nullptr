from rest_framework import serializers
from . import models
from dj_rest_auth.serializers import UserDetailsSerializer


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

class CustomUserDetailsSerializer(UserDetailsSerializer):
    user_type = serializers.CharField()
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('user_type', )