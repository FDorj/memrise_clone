from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class Exercise(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def evaluate_answers(self, user_answer):
        return self.answer.strip().lower() == user_answer.strip().lower()

    def get_feedback(self, user_answer):
        if self.evaluate_answers(user_answer):
            return "Correct!"
        else:
            return f"Incorrect. The correct answer is: {self.answer}"

    def __str__(self):
        return self.question

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    exercises = models.ManyToManyField(Exercise, related_name='lessons')

    def get_lesson_details(self):
        return {'title': self.title, 'content': self.content, 'exercises': self.exercises.all()}

    def load_lesson(self):
        return self.get_lesson_details()

    def __str__(self):
        return self.title

class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    completed_lessons = models.ManyToManyField(Lesson, through='LessonCompletion', related_name='completed_by')
    scores = models.JSONField(default=dict)

    def display_progress_summary(self):
        completed = self.completed_lessons.count()
        total_score = sum([comp.score for comp in LessonCompletion.objects.filter(user=self.user)])
        return {'completed_lessons': completed, 'total_score': total_score}

    def get_progress_summary(self):
        return self.display_progress_summary()

    def provide_recommendations(self):
        recommendations = Lesson.objects.exclude(id__in=self.completed_lessons.all())
        return recommendations

    def show_detailed_statistics(self):
        detailed_stats = LessonCompletion.objects.filter(user=self.user).values('lesson__title', 'score', 'completion_date')
        return detailed_stats

    def track_lesson(self, lesson, score):
        # Check if the lesson has already been completed
        if not LessonCompletion.objects.filter(user=self.user, lesson=lesson).exists():
            LessonCompletion.objects.create(progress=self, lesson=lesson, score=score, user=self.user)
            if lesson.title in self.scores:
                self.scores[lesson.title] += score
            else:
                self.scores[lesson.title] = score
            self.save()
        else:
            print(f"Lesson {lesson.title} already completed by {self.user.username}")

    def __str__(self):
        return f'Progress of {self.user.username}'

class LessonCompletion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, null=True, blank=True)
    completion_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} completed {self.lesson.title}'

class Search(models.Model):
    keywords = models.CharField(max_length=200)
    results = models.ManyToManyField(Lesson)

    def display_search_results(self):
        return self.results.all()

    def execute_search(self, keyword):
        self.results.set(Lesson.objects.filter(title__icontains=keyword))
        self.save()

    def __str__(self):
        return self.keywords
