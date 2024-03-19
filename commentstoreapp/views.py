from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from commentstoreapp.forms import InsertNewComment
from commentstoreapp.models import Comment
from register.forms import RegisterForm


@csrf_protect
def comment_store(request):
    form = InsertNewComment()

    if request.method == 'GET':
        headers = request.META
        for header_name, header_value in headers.items():
            print(f"{header_name}: {header_value}")

        return render(request, 'comment.html', {'new_comment': form})

    elif request.method == 'POST':
        name = request.POST.get('name')
        date = datetime.strptime(request.POST.get('visit_date'), '%d/%m/%Y').date()
        comment = request.POST.get('comment_str')

        t = Comment(name=name, visit_date=date, comment_str=comment)
        t.save()

        return render(request, 'home.html', {'cmnt_list': list(Comment.objects.all()), 'new_comment': form})

    else:
        return HttpResponse("Hello, Student. You're at the Comment Store Application.")


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully logged in.')
                return redirect('home')  # Change 'home' to the name of your homepage URL
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'login_user': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')  # Change 'home' to your desired URL after logout

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('login')  # Change 'home' to the name of your homepage URL
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'register_user': form})


def insert_new_comment(request):
    if request.method == 'POST':
        form = InsertNewComment(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            visit_date = form.cleaned_data['visit_date']
            comment_str = form.cleaned_data['comment_str']
            return redirect('home')
    else:
        form = InsertNewComment()

    return render(request, 'comment.html', {'new_comment': form})


def home(request):
    return render(request, "home.html", {'cmnt_list': list(Comment.objects.all())})
