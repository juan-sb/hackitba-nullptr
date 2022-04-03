from rest_framework import serializers
from . import models
from dj_rest_auth.serializers import UserDetailsSerializer
import pytube


class ProjectSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(
        source='like_set.count', 
        read_only=True
    )
    class Meta:
        model = models.Project
        fields = ['name', 'video_profile', 'video_description', 'description', 'like_count', 'pioneer', 'pk']

    def validate_video_profile(self, value):
        ytvideo = pytube.YouTube(value)
        if(ytvideo.length > 60):
            raise serializers.ValidationError("El video de perfil es demasiado largo")
        return ytvideo.embed_url

    def validate_video_description(self, value):
        ytvideo = pytube.YouTube(value)
        if(ytvideo.length > 180):
            raise serializers.ValidationError("El video de descripción es demasiado largo")
        return ytvideo.embed_url


class MatchSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = models.Match
        fields = "__all__"

class MatchCreateSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=models.Project.objects.all())
    class Meta:
        model = models.Match
        fields = "__all__"

class CustomUserDetailsSerializer(UserDetailsSerializer):
    user_type = serializers.CharField()
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('user_type', )

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'
    