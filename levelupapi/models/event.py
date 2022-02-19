from django.db import models

from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer


class Event(models.Model):
    
    organizer = models.ForeignKey(Gamer, null=True, on_delete=models.SET_NULL) 
    description = models.CharField(max_length=100, default="None")
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)