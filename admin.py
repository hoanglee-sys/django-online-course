from django.contrib import admin
# Đủ 7 class import theo yêu cầu con bot:
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
