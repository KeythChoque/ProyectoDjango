from rest_framework import serializers
from .models import CompetidoresModel, DojoModel

class CompetidoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetidoresModel
        fields = "__all__"

class DojoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DojoModel
        fields = "__all__"