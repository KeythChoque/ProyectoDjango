from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from deportista.models import CompetidoresModel, DojoModel

from .models import CampeonatoModel, CategoriaModel, ModalidadModel

CAMPEONATO_PAYLOAD = {
    "nombre": "Campeonato Nacional de Karate",
    "fecha_realizacion": "2026-11-20",
    "ranking": True,
    "departamento": "Lima",
    "provincia": "Lima",
    "distrito": "Miraflores",
}

CATEGORIA_PAYLOAD = {
    "nombre": "K4",
    "modalidad": "Kata",
    "tipo": "Individual",
    "nivel": "Avanzado",
}

DOJO_PAYLOAD = {
    "nombre": "Dojo Centro",
    "fecha_fundacion": "2012-01-01",
    "distrito": "Centro",
    "provincia": "Cusco",
    "departamento": "Cusco",
    "pais": "Peru",
    "jefe_instructor": "Sensei Kim",
}


class CampeonatoAPITestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("campeonato-list")

    def test_create_campeonato(self):
        response = self.client.post(self.list_url, CAMPEONATO_PAYLOAD, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CampeonatoModel.objects.count(), 1)

    def test_list_campeonatos(self):
        CampeonatoModel.objects.create(**CAMPEONATO_PAYLOAD)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_campeonato(self):
        campeonato = CampeonatoModel.objects.create(**CAMPEONATO_PAYLOAD)
        response = self.client.get(reverse("campeonato-detail", args=[campeonato.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nombre"], CAMPEONATO_PAYLOAD["nombre"])


class CategoriaAPITestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("categoria-list")

    def test_create_categoria(self):
        response = self.client.post(self.list_url, CATEGORIA_PAYLOAD, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CategoriaModel.objects.count(), 1)


class ModalidadAPITestCase(APITestCase):
    def setUp(self):
        self.dojo = DojoModel.objects.create(**DOJO_PAYLOAD)
        self.competidor = CompetidoresModel.objects.create(
            nombres="Luis",
            apellidos="Garcia",
            edad=15,
            sexo="M",
            dni="99999999",
            fecha_nacimiento="2011-05-10",
            grado="Cinta Verde",
            fecha_grado="2024-06-01",
            dojo=self.dojo,
        )
        self.campeonato = CampeonatoModel.objects.create(**CAMPEONATO_PAYLOAD)
        self.categoria = CategoriaModel.objects.create(**CATEGORIA_PAYLOAD)
        self.list_url = reverse("modalidad-list")
        self.payload = {
            "competidor": self.competidor.pk,
            "categoria": self.categoria.pk,
            "campeonato": self.campeonato.pk,
        }

    def test_create_modalidad(self):
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ModalidadModel.objects.count(), 1)

    def test_modalidad_str(self):
        modalidad = ModalidadModel.objects.create(
            competidor=self.competidor,
            categoria=self.categoria,
            campeonato=self.campeonato,
        )
        self.assertIsInstance(str(modalidad), str)
        self.assertIn(self.categoria.nombre, str(modalidad))

    def test_list_modalidades(self):
        ModalidadModel.objects.create(
            competidor=self.competidor,
            categoria=self.categoria,
            campeonato=self.campeonato,
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)