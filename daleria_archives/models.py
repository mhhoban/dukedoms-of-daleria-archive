from django.contrib.postgres.fields import JSONField
from django.db import models

class Card(models.Model):
    name = models.TextField(default='')
    type = models.TextField(default='')
    cost = models.IntegerField(default=0)
    treasure = models.IntegerField(default=0)
    victory_points = models.IntegerField(default=0)
    actions = JSONField()
