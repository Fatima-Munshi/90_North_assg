from django.urls import path
from .views import signup_view, login_view, chat_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('chat/<str:selected_user>/', chat_view, name='chat_with_user'),
    path('chat/', chat_view, name='chat'),
]
