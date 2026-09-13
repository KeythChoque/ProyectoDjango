from django.urls import path
from .views import (
    CampeonatoListCreateView,
    CampeonatoRetrieveUpdateDestroyView,
    CategoriaListCreateView,
    CategoriaRetrieveUpdateDestroyView,
    ModalidadListCreateView,
    ModalidadRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("campeonatos/", CampeonatoListCreateView.as_view(), name="campeonato-list"),
    path("campeonatos/<int:pk>/", CampeonatoRetrieveUpdateDestroyView.as_view(), name="campeonato-detail"),
    path("categorias/", CategoriaListCreateView.as_view(), name="categoria-list"),
    path("categorias/<int:pk>/", CategoriaRetrieveUpdateDestroyView.as_view(), name="categoria-detail"),
    path("modalidades/", ModalidadListCreateView.as_view(), name="modalidad-list"),
    path("modalidades/<int:pk>/", ModalidadRetrieveUpdateDestroyView.as_view(), name="modalidad-detail"),
]