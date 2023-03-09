from django.urls import path
from .views import game_1

urlpatterns = [
    path("game-1/", game_1, name="game-1"),
]
