from django.test import TestCase
from django.urls import reverse
from .models import User, Progress, Lesson, Exercise, LessonCompletion, Search

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

class ProgressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.progress = Progress.objects.create(user=self.user)

    def test_progress_creation(self):
        self.assertEqual(self.progress.user.username, 'testuser')

class LessonModelTest(TestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Lesson content.')

    def test_lesson_creation(self):
        self.assertEqual(self.lesson.title, 'Test Lesson')
        self.assertEqual(self.lesson.content, 'Lesson content.')

class ExerciseModelTest(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(question='What is 2+2?', answer='4')

    def test_exercise_creation(self):
        self.assertEqual(self.exercise.question, 'What is 2+2?')
        self.assertEqual(self.exercise.answer, '4')

    def test_exercise_evaluation(self):
        self.assertTrue(self.exercise.evaluate_answers('4'))
        self.assertFalse(self.exercise.evaluate_answers('5'))

class LessonCompletionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Lesson content.')
        self.completion = LessonCompletion.objects.create(user=self.user, lesson=self.lesson, score=100)

    def test_lesson_completion_creation(self):
        self.assertEqual(self.completion.user.username, 'testuser')
        self.assertEqual(self.completion.lesson.title, 'Test Lesson')
        self.assertEqual(self.completion.score, 100)

class SearchModelTest(TestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Lesson content.')
        self.search = Search.objects.create(keywords='Test')

    def test_search_execution(self):
        self.search.execute_search('Test')
        self.assertIn(self.lesson, self.search.display_search_results())

class SelectTopicViewTest(TestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Lesson content.')

    def test_select_topic_view(self):
        response = self.client.get(reverse('select_topic'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Lesson')

class ViewLessonViewTest(TestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Lesson content.')

    def test_view_lesson_view(self):
        response = self.client.get(reverse('view_lesson', args=[self.lesson.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lesson content.')

class CompleteExerciseViewTest(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(question='What is 2+2?', answer='4')

    def test_complete_exercise_view_get(self):
        response = self.client.get(reverse('complete_exercise', args=[self.exercise.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is 2+2?')

    def test_complete_exercise_view_post(self):
        response = self.client.post(reverse('complete_exercise', args=[self.exercise.id]), {'answer': '4'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Correct!')

class SearchLessonViewTest(TestCase):
    def test_search_lesson_view_get(self):
        response = self.client.get(reverse('search_lesson'))
        self.assertEqual(response.status_code, 200)

    def test_search_lesson_view_post(self):
        lesson = Lesson.objects.create(title='Test Lesson', content='Lesson content.')
        response = self.client.post(reverse('search_lesson'), {'keyword': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Lesson')

class ReviewProgressViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.progress = Progress.objects.create(user=self.user)

    def test_review_progress_view(self):
        response = self.client.get(reverse('review_progress', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
