from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('start_scheduler/', views.start_scheduler, name='start_scheduler'),
    path('stop_scheduler/', views.stop_scheduler, name='stop_scheduler'),

    # path('parse_news/', views.parse_and_save_news, name='parse_news'),
    path('run_puppeteer/', views.run_puppeteer, name='run_puppeteer'),
    path("get_news/", views.get_news_from_db, name="get_news"),
]
