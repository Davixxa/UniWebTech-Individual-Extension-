from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, LoginForm
from games.models import Genre

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, "genres": Genre.objects.all()})



def index(request):
    return redirect('/games/1')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        #orm = AuthenticationForm(request.)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request.user)
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, "genres": Genre.objects.all()})
    else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, "genres": Genre.objects.all()})

def logout_view(request):
    logout(request)
    return redirect('login')