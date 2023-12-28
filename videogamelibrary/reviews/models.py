from django.db import models
from games.models import Game
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Unknown Title")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    text = models.TextField(max_length=1000, blank=True, validators=[MaxLengthValidator(1000)])

    def __str__(self):
        return str(self.game) + ": " + str(self.rating)