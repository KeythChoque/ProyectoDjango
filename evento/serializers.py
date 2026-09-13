from rest_framework import serializers
from .models import CampeonatoModel, CategoriaModel, ModalidadModel


class CampeonatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampeonatoModel
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = "__all__"


class ModalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadModel
        fields = "__all__"