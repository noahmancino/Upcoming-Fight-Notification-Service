from django.db import models
from django.db.models import Q


class Fighter(models.Model):
    name = models.CharField(max_length=60)
    birth_date = models.IntegerField()
    sherdog_url = models.CharField(max_length=100)
    weight_class = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    @classmethod
    def exists_in_db(cls, fighter):
        return cls.objects.filter(name=fighter.name, birth_date=fighter.birth_date).exists()

    def __repr__(self):
        return str(self.__dict__)


class Match(models.Model):
    fighter1 = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="fighter_1")
    fighter2 = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="fighter_2")


class Event(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField()
    matches = models.ManyToManyField(Match)
