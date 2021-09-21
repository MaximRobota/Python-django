from django.contrib import admin

from .models import Question


class ChooseAdmin(admin.ModelAdmin):
    raw_id_fields = ['question']


class QuestionAdmin(admin.ModelAdmin):
    ordering = ['date_created']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['question']


# admin.site.register(Question, ChooseAdmin)
admin.site.register(Question)
