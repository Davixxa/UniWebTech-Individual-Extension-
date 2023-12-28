from django.urls import path
from . import views

urlpatterns = [
    path("<int:review_id>/", views.show_review, name="show_review"),
    path("create/<int:game_id>", views.compose_review, name="create_review"),
    path("update/<int:review_id>", views.update_review, name="update_review"),
    path("delete/<int:review_id>", views.delete_review, name="delete_review"),
]