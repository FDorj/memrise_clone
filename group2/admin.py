from django.contrib import admin
from .models import User, Progress, Lesson, Exercise, LessonCompletion, Search

class ExerciseInline(admin.TabularInline):
    model = Lesson.exercises.through  # Through table for many-to-many relationship

class LessonAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]
    list_display = ('title',)

admin.site.register(User)
admin.site.register(Progress)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exercise)
admin.site.register(LessonCompletion)
admin.site.register(Search)
