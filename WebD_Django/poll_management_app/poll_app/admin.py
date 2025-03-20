from django.contrib import admin
from .models import Poll, Choice, Vote

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('question',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote)
