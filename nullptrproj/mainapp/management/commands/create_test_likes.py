from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from mainapp.models import Like, Project, User


LIKES = [
    ('projectA', 'investor1'),
    ('projectB', 'investor1'),
    ('projectB', 'investor2'),
    ('projectC', 'investor1'),
    ('projectC', 'investor2'),
    ('projectC', 'investor3'),
    ('projectD', 'investor1'),
    ('projectD', 'investor2'),
    ('projectD', 'investor3'),
    ('projectD', 'investor4'),
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for l in LIKES:
            u = User.objects.filter(username=l[1]).get()
            p = Project.objects.filter(name=l[0]).get()
            lp = Like(investor=u, project=p)
            lp.save()