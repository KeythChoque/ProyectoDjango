from django.db import models

class DojoModel(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    fecha_fundacion = models.DateField()
    distrito = models.CharField(max_length=100, null=False, blank=False)
    provincia = models.CharField(max_length=100, null=False, blank=False)
    departamento = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)
    jefe_instructor = models.CharField(max_length=100, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "dojo"
        verbose_name = "Dojo"
        verbose_name_plural = "Dojos"

    def __str__(self):
        return self.nombre

class CompetidoresModel(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    edad = models.IntegerField(blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    dni = models.CharField(max_length=8, unique=True, null=False, blank=False)
    fecha_nacimiento = models.DateField()
    grado = models.CharField(max_length=50, null=False, blank=False)
    fecha_grado = models.DateField()

    dojo = models.ForeignKey(DojoModel,on_delete=models.PROTECT,related_name="dojo_p")

    class Meta:
        db_table = "competidores"
        verbose_name = "Competidores"
        verbose_name_plural = "Competidores"

    def __str__(self):
        return f"{self.dojo.nombre} - {self.nombres}"