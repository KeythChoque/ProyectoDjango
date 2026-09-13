from django.urls import path
from .views import (
    CompetidoresListCreateView,
    CompetidoresRetrieveUpdateDestroyView,
    DojoListCreateView,
    DojoRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("competidores/", CompetidoresListCreateView.as_view(), name="competidor-list"),
    path("competidores/<int:pk>/", CompetidoresRetrieveUpdateDestroyView.as_view(), name="competidor-detail"),
    path("dojos/", DojoListCreateView.as_view(), name="dojo-list"),
    path("dojos/<int:pk>/", DojoRetrieveUpdateDestroyView.as_view(), name="dojo-detail"),
]