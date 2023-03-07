from django.contrib import admin
from .models import Question


class QuestoinAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question,QuestoinAdmin)