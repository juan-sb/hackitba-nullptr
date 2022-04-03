from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import MatchSerializer, ProjectSerializer, CustomUserDetailsSerializer, MatchCreateSerializer
from .models import Match, Project, User
from rest_framework import generics
from django.db.models import Count, Exists, OuterRef
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

class FilteredViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class ProjectViewSet(FilteredViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if(user.user_type == user.UserType.PIONEER):
            queryset = Project.objects.filter(pioneer=user)
            #TODO magic ordering o_o
        else:
            queryset = Project.objects \
                .filter(~Exists(Match.objects.filter(investor=user, project_id=OuterRef('pk')))) \
                .annotate(like_count=Count('like')).order_by('-like_count')
        return queryset

class MatchViewSet(FilteredViewSet):
    #serializer_class = MatchSerializer

    def get_queryset(self):
        user = self.request.user
        if(user.user_type == user.UserType.PIONEER):
            queryset = Match.objects.filter(project__pioneer=user)
        else:
            queryset = Match.objects.filter(investor=user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return MatchCreateSerializer
        return MatchSerializer

def VueView(request):
    return render(request, 'mainapp/vue.html')

class UserViewSet(FilteredViewSet):    
    queryset = User.objects.all().order_by('id')
    serializer_class = CustomUserDetailsSerializer