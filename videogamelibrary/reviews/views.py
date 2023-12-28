from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review, Game
from django.contrib.auth.decorators import login_required
from games.models import Genre

# Create your views here.

def compose_review(request, game_id):
    # This one has blocking logic on the template so I don't really care too much.
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.game = Game.objects.get(pk=game_id)
            review.save()
            messages.success(request, ("Review successfully posted"))
            return HttpResponseRedirect('/reviews/{}'.format(review.id))
    else:
        form = ReviewForm
    return render(request, 'create_review.html',  {"form": form, "genres": Genre.objects.all()})

def update_review(request, review_id):
    # This one also has blocking logic on the template so I don't really care too much here either.
    review = Review.objects.get(pk=review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        messages.success(request, ("Review successfully updated"))
        return HttpResponseRedirect('/reviews/{}'.format(review.id))

    return render(request, 'update_review.html', {'review': review, 'form': form, "genres": Genre.objects.all()})


def delete_review(request, review_id):
    # This one however, doesn't, and therefore I should REALLY care.
    review = Review.objects.get(pk=review_id)
    if request.user != review.user:
        messages.success(request, ("Nice try. Sorry, takes more than a manual URL entry to fool us."))
        return HttpResponseRedirect('/reviews/{}'.format(review_id))    
    game=review.game.id
    review.delete()
    messages.success(request, ("Review successfully deleted"))
    return HttpResponseRedirect('/games/{}'.format(game))


def show_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    return render(request, 'review.html', {'review': review, "genres": Genre.objects.all()})