
from django.contrib import admin
from django.urls import path, include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('login/', views.login_view, name='login'),  
    path('chat/<str:selected_user>/', views.chat_view, name='chat_with_user'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.home, name='home'),
]
