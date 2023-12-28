from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from games.models import Genre

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.success(request, ("There was an error logging you in. Double check your credentials and try again."))
            return redirect('login')
    else:
        return render(request, 'login.html', {"genres": Genre.objects.all()})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have successfully been logged out."))
    return redirect('login')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            #email = form.cleaned_data["email"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form, "genres": Genre.objects.all()})