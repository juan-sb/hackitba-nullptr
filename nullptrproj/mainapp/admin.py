from dataclasses import fields
from django.contrib import admin
from .models import Angel, Pioneer, Match, Like, Investment, Project

class AngelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Angel._meta.fields if field.name != "id"]

class PioneerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pioneer._meta.fields if field.name != "id"]

class MatchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Match._meta.fields if field.name != "id"]

class LikeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Like._meta.fields if field.name != "id"]

class InvestmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Investment._meta.fields if field.name != "id"]

class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields if field.name != "id"]


admin.site.register(Angel, AngelAdmin)
admin.site.register(Pioneer, PioneerAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(Project, ProjectAdmin)