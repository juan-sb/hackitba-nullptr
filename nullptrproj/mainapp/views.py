from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import MatchSerializer, ProjectSerializer, CustomUserDetailsSerializer, MatchCreateSerializer, LikeSerializer
from .models import Match, Project, User, Like
from rest_framework import generics
from django.db.models import Count, Exists, OuterRef
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse

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

class LikeViewSet(FilteredViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        user = self.request.user
        if(user.user_type == user.UserType.PIONEER):
            queryset = Like.objects.filter(project__pioneer=user)
        else:
            queryset = Like.objects.filter(investor=user)
        return queryset


def swapLike(request, project_param):
    p = Project.objects.get(pk=project_param)
    l = Like.objects.filter(project=p).filter(investor=request.user).all()
    if(l.__len__() > 0):
        l.delete()
        s = "deleted"
    else :
        l = Like(project=p, investor=request.user)
        l.save()
        s = "created"
    return HttpResponse(s)