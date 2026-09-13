from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics

from .models import CompetidoresModel, DojoModel
from .serializers import CompetidoresSerializer, DojoSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Listar competidores",
        description=(
            "Devuelve el listado de todos los competidores registrados, "
            "incluyendo el id de su dojo de pertenencia."
        ),
    ),
    post=extend_schema(
        summary="Registrar competidor",
        description=(
            "Crea un nuevo competidor. El campo `dni` es único y `sexo` solo "
            "admite 'M' (masculino) o 'F' (femenino). El dojo se indica por su id."
        ),
    ),
)
class CompetidoresListCreateView(generics.ListCreateAPIView):
    queryset = CompetidoresModel.objects.all()
    serializer_class = CompetidoresSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Obtener competidor",
        description="Devuelve los datos de un competidor específico según su id.",
    ),
    put=extend_schema(
        summary="Actualizar competidor",
        description="Reemplaza por completo los datos de un competidor (PUT).",
    ),
    patch=extend_schema(
        summary="Actualizar parcialmente competidor",
        description=(
            "Actualiza solo los campos enviados de un competidor (PATCH). "
            "Útil para corregir un campo sin reenviar todo el registro."
        ),
    ),
    delete=extend_schema(
        summary="Eliminar competidor",
        description=(
            "Elimina un competidor. No se puede eliminar si está asociado a "
            "una modalidad (integridad PROTECT)."
        ),
    ),
)
class CompetidoresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompetidoresModel.objects.all()
    serializer_class = CompetidoresSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Listar dojos",
        description="Devuelve el listado de todos los dojos (escuelas de karate) registrados.",
    ),
    post=extend_schema(
        summary="Registrar dojo",
        description=(
            "Crea un nuevo dojo con sus datos de ubicación "
            "(distrito, provincia, departamento, país) y su jefe de instructor."
        ),
    ),
)
class DojoListCreateView(generics.ListCreateAPIView):
    queryset = DojoModel.objects.all()
    serializer_class = DojoSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Obtener dojo",
        description="Devuelve los datos de un dojo específico según su id.",
    ),
    put=extend_schema(
        summary="Actualizar dojo",
        description="Reemplaza por completo los datos de un dojo (PUT).",
    ),
    patch=extend_schema(
        summary="Actualizar parcialmente dojo",
        description="Actualiza solo los campos enviados de un dojo (PATCH).",
    ),
    delete=extend_schema(
        summary="Eliminar dojo",
        description=(
            "Elimina un dojo. No se puede eliminar si tiene competidores "
            "asociados (integridad PROTECT)."
        ),
    ),
)
class DojoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DojoModel.objects.all()
    serializer_class = DojoSerializer