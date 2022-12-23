from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceAdminInline(admin.TabularInline):
    model = Choice
    fields = ('choice_text',)


class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceAdminInline,)


admin.site.register(Question, QuestionAdmin)
