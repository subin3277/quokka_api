from rest_framework import serializers
from .models import Quokka

class QuokkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quokka
        fields = ('data',)