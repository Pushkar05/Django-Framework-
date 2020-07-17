from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id','question_text','c1','c2','c3','c4','answer','marks')


admin.site.register(Question,QuestionAdmin)

# Register your models here.
