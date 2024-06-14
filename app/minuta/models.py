from django.db import models

class MinutasCasei(models.Model):
    titulominuta = models.CharField("Titulo de la Minuta",max_length=200)
    fechaminuta = models.DateField("Fecha de la Minuta")
    minuta = models.TextField("Minuta")
    acuerdos = models.TextField("Acuerdos")

    def __str__(self):
        return self.titulominuta

class UserMinuta(models.Model):
    caseiuser = models.ForeignKey('usuario.CaseiUser', verbose_name=("UsuarioCasei"), on_delete=models.CASCADE)
    minuta = models.ForeignKey('minuta.MinutasCasei', verbose_name=("MinutaCasei"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.caseiuser.username} en {self.minuta.titulominuta}"

