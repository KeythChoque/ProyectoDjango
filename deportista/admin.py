from django.contrib import admin
from .models import CompetidoresModel, DojoModel


@admin.register(DojoModel)
class DojoModelAdmin(admin.ModelAdmin):
    list_display = ("nombre", "distrito", "provincia", "departamento", "pais", "jefe_instructor")
    search_fields = ("nombre", "jefe_instructor", "distrito")


@admin.register(CompetidoresModel)
class CompetidoresModelAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "dni", "edad", "sexo", "dojo")
    search_fields = ("nombres", "apellidos", "dni")
    list_filter = ("sexo", "dojo")