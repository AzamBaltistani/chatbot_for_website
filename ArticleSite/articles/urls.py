from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('article/<int:article_id>/', views.article_view, name='article_view'),
]
