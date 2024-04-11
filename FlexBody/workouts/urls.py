from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', views.create_workout, name='create_workout'),    
    path('workout/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('exercise/<int:category_id>/', views.exercise, name='exercise'),
    path('my_workout/', views.my_workout, name='my_workout'),
    path('workouts_list/', views.workouts_list, name='workouts_list'),
    path('workouts/delete/<int:workout_id>/', views.delete_workout, name='delete_workout'),
    path('exercise/details/<int:selected_exercise_id>/', views.exercise_detail, name='exercise_detail'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)