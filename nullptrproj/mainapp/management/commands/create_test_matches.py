from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from mainapp.models import User, Project, Match


MATCHES = [
    ('projectA', 'investor1'),
    ('projectB', 'investor1'),
    ('projectB', 'investor2'),
    ('projectC', 'investor1'),
    ('projectC', 'investor2'),
    ('projectD', 'investor2'),
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for m in MATCHES:
            u = User.objects.filter(username=m[1]).get()
            p = Project.objects.filter(name=m[0]).get()
            um = Match(investor=u, project=p)
            um.save()