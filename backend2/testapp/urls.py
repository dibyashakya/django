from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    # path('january/', views.january, name='january'),
    # path('february/', views.february, name='february'),
    path('<int:month>/', views.monthly_challenge_by_number, name="monthly_challenge_by_num"),
    path('<str:month>/', views.monthly_challenge, name="monthly_challenge"),
    # path('<month>/',views.monthly_challenge, name='monthly_challenge'),
]