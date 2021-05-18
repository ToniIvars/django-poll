from django.contrib import admin
from .models import Poll, PollAnswer, PollQuestion

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    
class PollQuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'poll')

class PollAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question')

admin.site.register(Poll, PollAdmin)
admin.site.register(PollQuestion, PollQuestionAdmin)
admin.site.register(PollAnswer, PollAnswerAdmin)