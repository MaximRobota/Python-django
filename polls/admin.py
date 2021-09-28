from django.contrib import admin

from .models import Question, Choice


class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ['question']


admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None, {'fields': ['question_text', 'description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

