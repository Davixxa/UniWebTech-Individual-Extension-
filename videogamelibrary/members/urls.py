from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    #path("<int:game_id>/", views.game, name="game"),¨
    path('login_user', views.login_user, name="login"), 
    path('logout_user', views.logout_user, name="logout"), 
    path('register_user', views.register_user, name="register"),
]