from django.urls import path
from . import views

urlpatterns = [
    path('interview/', views.interview_page, name='interview_page'),
    path('get-question/', views.get_next_question, name='get_question'),
    path('evaluate-answer/', views.evaluate_user_answer, name='evaluate_answer'),
    path('', views.interview_page, name='interview'),
    path('get_next_question/', views.get_next_question, name='get_next_question'),
]
