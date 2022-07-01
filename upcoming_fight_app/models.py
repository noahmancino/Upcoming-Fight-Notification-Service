from django.db import models
from django.db.models import Q


class Fighter(models.Model):
    name = models.CharField(max_length=60)
    oldest_possible_birthday = models.IntegerField()  # Ages change, so I'd prefer to derive ages from birthdays
    youngest_possible_birthday = models.IntegerField()
    weight_class = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    @classmethod
    def exists_by_name_and_birthdays(cls, fighter_name, youngest, oldest):
        return cls.objects.filter(Q(youngest_possible_birthday__in=[youngest, oldest]) |
                                  Q(youngest_possible_birthday__in=[youngest, oldest]), name=fighter_name) \
            .count()


class Match(models.Model):
    fighter1 = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="fighter_1")
    fighter2 = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="fighter_2")


class Event(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField()
    matches = models.ManyToManyField(Match)
