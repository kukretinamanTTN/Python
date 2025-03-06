from django.contrib import admin
from temp_app.models import Question, Choice

def reset_votes(modeladmin, request, queryset):
    queryset.update(votes=0)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    search_fields = ('text',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','text','votes')
    actions = [reset_votes]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)