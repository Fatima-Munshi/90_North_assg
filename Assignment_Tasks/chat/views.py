from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('chat')
    return render(request, 'chat/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
        return render(request, 'chat/login.html')
    
    
@login_required
def chat_view(request, selected_user=None):
        users = User.objects.exclude(username=request.user.username)
        selected_user_instance = User.objects.get(username=selected_user) if selected_user else None
        messages = Message.objects.filter(receiver=request.user, sender=selected_user_instance) | Message.objects.filter(receiver=selected_user_instance, sender=request.user)
        return render(request, 'chat/chat.html', {'users': users, 'messages': messages, 'selected_user': selected_user_instance})

def home(request):
    return render(request, 'chat/home.html')