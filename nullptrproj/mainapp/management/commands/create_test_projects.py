from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from mainapp.models import Project, User


PROJECTS = [
    ('projectA', 'pioneer1', 'IoT is good'),
    ('projectB', 'pioneer2', 'AI is good'),
    ('projectC', 'pioneer2', 'afshr is bad'),
    ('projectD', 'pioneer2', 'that is very happy'),
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for p in PROJECTS:
            u = User.objects.filter(username=p[1]).get()
            up = Project(name=p[0], pioneer=u, description=p[2])
            up.save()