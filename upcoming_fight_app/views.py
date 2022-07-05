from upcoming_fight_app.models import Fighter
from upcoming_fight_app.serializers import FighterSerializer
from rest_framework import generics


class FighterList(generics.ListCreateAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer

