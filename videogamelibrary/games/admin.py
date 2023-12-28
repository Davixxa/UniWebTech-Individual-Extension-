from django.contrib import admin

# Register your models here.

from .models import Game, Developer, Genre

admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Genre)