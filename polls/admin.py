from django.contrib import admin
from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    """Create question for poll."""

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date', 'end_date'], 'classes': ['collapse']}), ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class ChoiceInline(admin.TabularInline):
    """Create choice for poll."""

    model = Choice
    extra = 3


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
