from django.contrib import admin
from .models import User, Progress, Lesson, Exercise, LessonCompletion, Search

admin.site.register(User)
admin.site.register(Progress)
admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(LessonCompletion)
admin.site.register(Search)
