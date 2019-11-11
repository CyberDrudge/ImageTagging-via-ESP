from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PlayerManager(models.Manager):
    def new_or_get(self, user):
        qs = self.get_queryset().filter(user=user)
        new_obj = False
        if qs.count() == 1:
            player_obj = qs.first()
        else:
            new_obj = True
            player_obj = Player.objects.create(user=user, current_task=None)
        return player_obj, new_obj


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    current_task = models.PositiveIntegerField(null=True)

    objects = PlayerManager()

    def __str__(self):
        return self.user.username
