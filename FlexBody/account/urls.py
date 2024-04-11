from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sign-up', views.sign_up, name='sign-up'),
    path('log-in', views.log_in, name='log-in'),
    path('log-out', views.log_out, name='log-out'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)