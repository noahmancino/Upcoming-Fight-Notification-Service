from django.db import models


class Fighter(models.Model):
    name = models.CharField(max_length=60)
    birth_range = models.CharField(max_length=10)
    weight_class = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50, blank=True, null=True)


class Match(models.Model):
    fighter1 = models.ForeignKey(Fighter, on_delete=models.CASCADE)
    fighter1 = models.ForeignKey(Fighter, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField()
    matches = models.ManyToManyField(Match)
