from rest_framework import serializers
from upcoming_fight_app.models import Fighter


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = ['id', 'name', 'birth_date', 'sherdog_url', 'weight_class', 'nickname']
