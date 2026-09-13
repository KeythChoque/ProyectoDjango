from django.contrib import admin
from .models import CampeonatoModel, CategoriaModel, ModalidadModel


@admin.register(CampeonatoModel)
class CampeonatoModelAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_realizacion", "ranking", "departamento", "provincia", "distrito")
    search_fields = ("nombre", "departamento", "provincia", "distrito")


@admin.register(CategoriaModel)
class CategoriaModelAdmin(admin.ModelAdmin):
    list_display = ("nombre", "modalidad", "tipo", "nivel")
    search_fields = ("nombre", "modalidad", "tipo", "nivel")


@admin.register(ModalidadModel)
class ModalidadModelAdmin(admin.ModelAdmin):
    list_display = ("competidor", "categoria", "campeonato")
    search_fields = ("competidor__nombres", "competidor__apellidos", "categoria__nombre", "campeonato__nombre")