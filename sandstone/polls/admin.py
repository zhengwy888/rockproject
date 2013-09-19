from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
  #fields = ['question', 'pub_date']
  inlines = [ChoiceInline]
  list_display = ('question', 'pub_date')
  search_fields = ['question']
  
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)