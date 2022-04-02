from email.policy import default
from django.db import models
from django.db.models import IntegerField, URLField, TextField, CharField, DecimalField, BooleanField, ForeignKey
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    class UserType(models.TextChoices):
        INVESTOR = 'IN', _('Investor')
        PIONEER = 'PI', _('Pioneer')
        
    user_type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.PIONEER)

    def __str__(self):
        return self.username


def limit_to_investors():
    return {'user_type': User.UserType.INVESTOR}

def limit_to_pioneers():
    return {'user_type': User.UserType.PIONEER}



class Project(models.Model):
    name = CharField(max_length=30)
    pioneer = ForeignKey(User, limit_choices_to=limit_to_pioneers, on_delete=models.CASCADE)
    video_profile = URLField()
    video_description = URLField()
    description = CharField(max_length=512)
    hasEnded = BooleanField(default=False)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return "%s by %s"%(self.name, self.pioneer.username)


class Investment(models.Model):
    project = ForeignKey(Project, on_delete=models.CASCADE)
    investor = ForeignKey(User, limit_choices_to=limit_to_investors, on_delete=models.CASCADE)
    amount = DecimalField(max_digits = 10, decimal_places = 0)

    class Meta:
        verbose_name = _('Investment')
        verbose_name_plural = _('Investments')


class Match(models.Model):
    investor = ForeignKey(User, limit_choices_to=limit_to_investors, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)
    hasEnded = BooleanField(default = False)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')


class Like(models.Model):
    investor = ForeignKey(User, limit_choices_to=limit_to_investors, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)
    isPublic = BooleanField(default = False)

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')