from django.shortcuts import render, get_object_or_404
from .models import Lesson, Exercise, Progress, Search, User

def select_topic(request):
    lessons = Lesson.objects.all()
    return render(request, 'group2/select_topicc.html', {'lessons': lessons})

def view_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'group2/view_lesson.html', {'lesson': lesson})

def complete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    feedback = None
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        feedback = exercise.get_feedback(user_answer)
        user = request.user
        score = 1 if exercise.evaluate_answers(user_answer) else 0
        user.progress.track_lesson(exercise.lessons.first(), score)
    return render(request, 'group2/complete_exercise.html', {'exercise': exercise, 'feedback': feedback})

def search_lesson(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        search = Search.objects.create(keywords=keyword)
        search.execute_search(keyword)
        return render(request, 'group2/search_results.html', {'results': search.display_search_results()})
    return render(request, 'group2/search.html')

def review_progress(request, user_id):
    progress = get_object_or_404(Progress, user_id=user_id)
    summary = progress.get_progress_summary()
    detailed_stats = progress.show_detailed_statistics()
    recommendations = progress.provide_recommendations()
    return render(request, 'group2/review_progress.html', {
        'summary': summary,
        'detailed_stats': detailed_stats,
        'recommendations': recommendations
    })
