from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Game, Genre
from reviews.models import Review

#def index(request):
 #   return HttpResponse("Hello, world.")


def game(request, game_id):
    try:
        game_obj = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Game doesn't exist")
    return render(request, "game.html", {
        "genres": Genre.objects.all(),
        "reviews": Review.objects.filter(game=game_obj),
        "game": game_obj
    })

def index(request):
    return render(request, "games_list.html", {
        "genres": Genre.objects.all(),
        "games": Game.objects.all()
    })


def search(request):
    if request.method == "POST":
        query = request.POST["search"]  
        return render(request, "games_list.html", {
            "genres": Genre.objects.all(),
            "view": "search",
            "query": query,
            "games": Game.objects.filter(name__icontains=query),
        })



def genre(request, genre_id):
    try: 
        genre_obj = Genre.objects.get(pk=genre_id)
    except:
        raise Http404("Genre doesn't exist")
    return render(request, "games_list.html", {
        "genres": Genre.objects.all(),
        "view": "genre",
        "genre": genre_obj,
        "games": Game.objects.filter(genre=genre_obj)
    })

# Create your views here.
