from django.db import models

class CampeonatoModel(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    fecha_realizacion = models.DateField()
    ranking = models.BooleanField(default=False)
    departamento = models.CharField(max_length=50, null=False, blank=False)
    provincia = models.CharField(max_length=50, null=False, blank=False)
    distrito = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = "campeonato"
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"

    def __str__(self):
        return self.nombre

class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=10, null=False, blank=False)
    modalidad = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=10, null=False, blank=False)
    nivel = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = "categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre


class ModalidadModel(models.Model):
    competidor = models.ForeignKey("deportista.CompetidoresModel", on_delete=models.PROTECT, related_name = "competidores_p")
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.PROTECT, related_name="categorias_p")
    campeonato = models.ForeignKey(CampeonatoModel, on_delete=models.PROTECT, related_name="campeonato_p")

    class Meta:
        db_table = "modalidades"
        verbose_name = "Modalidades"

    def __str__(self):
        return f"{self.competidor} - {self.categoria} - {self.campeonato}"