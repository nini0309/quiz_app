from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = "welcome"),
    path('quiz/', views.quiz_page, name = "quiz"),
    path('results/<str:pk>', views.result_page, name = "results")
]