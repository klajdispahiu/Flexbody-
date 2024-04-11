from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise, Category
from django.conf import settings
from django.contrib.auth.models import User

@login_required
def create_workout(request):   
    categories = Category.objects.all()
    return render(request, 'workouts/create_workout.html', {'categories': categories})
    
@login_required
def exercise(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id)
    exercises = selected_category.exercises.all()
    return render(
        request,
        'workouts/exercise.html',
        {
            'selected_category': selected_category,
            'exercises': exercises
        }
    )

@login_required
def my_workout(request):
    if request.method == 'POST':
        workout_name = request.POST.get('workout_name')
        selected_exercise_ids = request.POST.getlist('selected_exercise')
        if selected_exercise_ids:
            workout = Workout.objects.create(name=workout_name, user=request.user)
            workout.exercises.set(selected_exercise_ids)
            return render(request, 'core/index.html')
    else:
        workouts = Workout.objects.filter(user=request.user)
        return render(request, 'workouts/workouts_list.html', {'workouts': workouts})

@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.user == workout.user:
        workout.delete()
    return redirect('index')

@login_required
def workouts_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/workouts_list.html', {'workouts': workouts})

    
@login_required
def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})

def exercise_detail(request, selected_exercise_id):
    exercise = Exercise.objects.get(id=selected_exercise_id)
    return render(request, 'workouts/exercise_detail.html', {'selected_exercise': exercise})
    
