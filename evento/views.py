from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics

from .models import CampeonatoModel, CategoriaModel, ModalidadModel
from .serializers import (
    CampeonatoSerializer,
    CategoriaSerializer,
    ModalidadSerializer,
)


@extend_schema_view(
    get=extend_schema(
        summary="Listar campeonatos",
        description="Devuelve el listado de todos los campeonatos registrados.",
    ),
    post=extend_schema(
        summary="Registrar campeonato",
        description=(
            "Crea un nuevo campeonato con su fecha de realización, ubicación "
            "y el indicador `ranking` (false por defecto) para determinar si "
            "afecta el ranking de los competidores."
        ),
    ),
)
class CampeonatoListCreateView(generics.ListCreateAPIView):
    queryset = CampeonatoModel.objects.all()
    serializer_class = CampeonatoSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Obtener campeonato",
        description="Devuelve los datos de un campeonato específico según su id.",
    ),
    put=extend_schema(
        summary="Actualizar campeonato",
        description="Reemplaza por completo los datos de un campeonato (PUT).",
    ),
    patch=extend_schema(
        summary="Actualizar parcialmente campeonato",
        description="Actualiza solo los campos enviados de un campeonato (PATCH).",
    ),
    delete=extend_schema(
        summary="Eliminar campeonato",
        description=(
            "Elimina un campeonato. No se puede eliminar si tiene modalidades "
            "asociadas (integridad PROTECT)."
        ),
    ),
)
class CampeonatoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CampeonatoModel.objects.all()
    serializer_class = CampeonatoSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Listar categorías",
        description="Devuelve el listado de todas las categorías registradas.",
    ),
    post=extend_schema(
        summary="Registrar categoría",
        description=(
            "Crea una nueva categoría definiendo su nombre, modalidad, tipo "
            "y nivel de la competencia."
        ),
    ),
)
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Obtener categoría",
        description="Devuelve los datos de una categoría específica según su id.",
    ),
    put=extend_schema(
        summary="Actualizar categoría",
        description="Reemplaza por completo los datos de una categoría (PUT).",
    ),
    patch=extend_schema(
        summary="Actualizar parcialmente categoría",
        description="Actualiza solo los campos enviados de una categoría (PATCH).",
    ),
    delete=extend_schema(
        summary="Eliminar categoría",
        description=(
            "Elimina una categoría. No se puede eliminar si está asociada a "
            "una modalidad (integridad PROTECT)."
        ),
    ),
)
class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Listar modalidades",
        description=(
            "Devuelve el listado de todas las modalidades (inscripciones de un "
            "competidor en una categoría dentro de un campeonato)."
        ),
    ),
    post=extend_schema(
        summary="Registrar modalidad",
        description=(
            "Crea una modalidad relacionando un competidor, una categoría y un "
            "campeonato (los tres se indican por su id)."
        ),
    ),
)
class ModalidadListCreateView(generics.ListCreateAPIView):
    queryset = ModalidadModel.objects.all()
    serializer_class = ModalidadSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Obtener modalidad",
        description="Devuelve los datos de una modalidad específica según su id.",
    ),
    put=extend_schema(
        summary="Actualizar modalidad",
        description="Reemplaza por completo los datos de una modalidad (PUT).",
    ),
    patch=extend_schema(
        summary="Actualizar parcialmente modalidad",
        description="Actualiza solo los campos enviados de una modalidad (PATCH).",
    ),
    delete=extend_schema(
        summary="Eliminar modalidad",
        description="Elimina la inscripción/modalidad de un competidor.",
    ),
)
class ModalidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModalidadModel.objects.all()
    serializer_class = ModalidadSerializer