from django.contrib import admin

# Register your models here.
from questions.models import Question, Answer, Profile, Tag


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'rating')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Profile)
admin.site.register(Tag)