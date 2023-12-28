from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="games_index"),
    path("<int:game_id>/", views.game, name="game"),
    path("genre/<int:genre_id>", views.genre, name="genre"),
    path("search/", views.search, name="search_games")
]