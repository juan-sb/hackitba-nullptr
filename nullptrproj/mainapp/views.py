from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import MatchSerializer, ProjectSerializer
from .models import Match, Project
from rest_framework import generics
from django.db.models import Count
from django.shortcuts import render

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if(user.user_type == user.UserType.PIONEER):
            queryset = Project.objects.filter(pioneer=user)
            #TODO magic ordering o_o
        else:
            #queryset = Project.objects.all()
            queryset = Project.objects.all().annotate(like_count=Count('like'))
            queryset = queryset.order_by('-like_count')
        return queryset


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer

    def get_queryset(self):
        user = self.request.user
        if(user.user_type == user.UserType.PIONEER):
            queryset = Match.objects.filter(project__pioneer=user)
            #TODO magic ordering o_o
        else:
            queryset = Match.objects.filter(investor=user)
        return queryset

def VueView(request):
    return render(request, 'mainapp/vue.html')