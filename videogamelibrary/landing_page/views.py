from django.shortcuts import render
from django.http import HttpResponse, Http404
from games.models import Game, Genre
from reviews.models import Review

# Create your views here.

def index(request):
    return render(request, 'home.html', {
        'recent_games': Game.objects.order_by('-id')[:8],
        'recent_reviews': Review.objects.order_by('-id')[:8],
    })