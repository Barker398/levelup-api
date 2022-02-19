from django.db import models

class SignUp(models.Model):
    
    game_event = models.ForeignKey("levelupapi.Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.CASCADE)