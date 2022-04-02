from django.db import models
from django.db.models import IntegerField, URLField, TextField, CharField, DecimalField, BooleanField, ForeignKey
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Pioneer(models.Model):
    video = URLField()
    user = ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Pioneer')
        verbose_name_plural = _('Pioneers')

    def __str__(self):
        return self.user.first_name


class Angel(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Angel')
        verbose_name_plural = _('Angels')

    def __str__(self):
        return self.user.first_name


class Project(models.Model):
    name = CharField(max_length=30)
    pioneer = ForeignKey(Pioneer, on_delete=models.CASCADE)
    video = URLField()
    resumen = CharField(max_length=512)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return "%s by %s"%(self.name, self.pioneer.user.name)


class Investment(models.Model):
    project = ForeignKey(Project, on_delete=models.CASCADE)
    angel = ForeignKey(Angel, on_delete=models.CASCADE)
    amount = DecimalField(max_digits = 10, decimal_places = 0)

    class Meta:
        verbose_name = _('Investment')
        verbose_name_plural = _('Investments')


class Match(models.Model):
    angel = ForeignKey(Angel, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)
    hasEnded = BooleanField(default = False)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')


class Like(models.Model):
    angel = ForeignKey(Angel, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)
    isPublic = BooleanField(default = False)

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')