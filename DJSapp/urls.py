from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('start_scheduler/', views.start_scheduler, name='start_scheduler'),
    path('stop_scheduler/', views.stop_scheduler, name='stop_scheduler'),
]
