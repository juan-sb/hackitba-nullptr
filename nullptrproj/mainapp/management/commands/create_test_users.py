from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from mainapp.models import User


USERS = [
    ('pioneer1', User.UserType.PIONEER),
    ('pioneer2', User.UserType.PIONEER),
    ('investor1', User.UserType.INVESTOR),
    ('investor2', User.UserType.INVESTOR),
    ('investor3', User.UserType.INVESTOR),
    ('investor4', User.UserType.INVESTOR),
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for u in USERS:
            User.objects.create_user(username=u[0], email="%s@%s.com"%(u[0], u[0]), user_type=u[1], password=u[0])
            #up = User(username=u[0], user_type=u[1], password=u[0])
            #up.save()