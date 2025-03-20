from django.contrib import admin
from temp_app.models import Question, Choice, Vote


@admin.action(description="Clear all votes")
def clear_votes(modeladmin, request, queryset):
    # Reset all vote counts to zero
    Choice.objects.update(votes=0)
    # Delete all Vote records
    Vote.objects.all().delete()

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    search_fields = ('text',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','text','votes')
    actions = [clear_votes]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote)