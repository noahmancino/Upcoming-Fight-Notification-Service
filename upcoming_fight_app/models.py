from django.db import models

class Fighter(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    weight_class = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50, blank=True, null=True)