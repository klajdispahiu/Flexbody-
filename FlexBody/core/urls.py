from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),

    # path('about/', views.about, name = 'about' )
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)