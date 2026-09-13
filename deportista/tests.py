from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CompetidoresModel, DojoModel

DOJO_PAYLOAD = {
    "nombre": "Dojo San Juan",
    "fecha_fundacion": "2010-05-10",
    "distrito": "San Juan",
    "provincia": "Lima",
    "departamento": "Lima",
    "pais": "Peru",
    "jefe_instructor": "Sensei Tanaka",
}


class DojoAPITestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("dojo-list")

    def test_create_dojo(self):
        response = self.client.post(self.list_url, DOJO_PAYLOAD, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DojoModel.objects.count(), 1)

    def test_list_dojos(self):
        DojoModel.objects.create(**DOJO_PAYLOAD)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_dojo(self):
        dojo = DojoModel.objects.create(**DOJO_PAYLOAD)
        response = self.client.get(reverse("dojo-detail", args=[dojo.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nombre"], DOJO_PAYLOAD["nombre"])


class CompetidoresAPITestCase(APITestCase):
    def setUp(self):
        self.dojo = DojoModel.objects.create(**DOJO_PAYLOAD)
        self.list_url = reverse("competidor-list")
        self.payload = {
            "nombres": "Ana",
            "apellidos": "Perez",
            "edad": 12,
            "sexo": "F",
            "dni": "12345678",
            "fecha_nacimiento": "2014-03-20",
            "grado": "Cinta Amarilla",
            "fecha_grado": "2024-06-01",
            "dojo": self.dojo.pk,
        }

    def test_create_competidor(self):
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CompetidoresModel.objects.count(), 1)

    def test_duplicate_dni_rejected(self):
        self.client.post(self.list_url, self.payload, format="json")
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_sexo_rejected(self):
        payload = {**self.payload, "sexo": "X", "dni": "87654321"}
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_detail_competidor(self):
        payload = {field: value for field, value in self.payload.items() if field != "dojo"}
        competidor = CompetidoresModel.objects.create(dojo=self.dojo, **payload)
        response = self.client.get(reverse("competidor-detail", args=[competidor.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)