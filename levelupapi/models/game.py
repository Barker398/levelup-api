from django.db import models
from .gamer import Gamer
from .gametype import GameType

class Game(models.Model):
   
    title = models.CharField(max_length=50, default="None")
    maker = models.CharField(max_length=75, default="None")
    gamer = models.ForeignKey(Gamer, null=True, on_delete=models.SET_NULL)
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.IntegerField(default=1)