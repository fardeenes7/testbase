from django.contrib import admin
from exam.models import Class, Exam, Question, Option, AnswerSheet, Answer

class ExamInline(admin.TabularInline):
    model = Exam
    extra = 0

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('teacher',)
    search_fields = ('name', 'teacher')
    inlines = [ExamInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'classes', 'date', 'start_time', 'end_time', 'duration')
    list_filter = ('classes', 'date')
    search_fields = ('name', 'classes')
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'question', 'question_type', 'mark')
    list_filter = ('exam', 'question_type')
    search_fields = ('exam', 'question_type')


class AnswerInline(admin.TabularInline):
    model = Answer
    extra=0

class AnswerSheetAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'status')
    list_filter = ('student', 'exam', 'status')
    search_fields = ('student', 'exam')
    inlines = [AnswerInline]

admin.site.register(Class, ClassAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(AnswerSheet, AnswerSheetAdmin)
admin.site.register(Answer)