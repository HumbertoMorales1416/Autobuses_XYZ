from django.db import models
import datetime

class Estatus_Unidad(models.Model):
  abreviacion = models.CharField(max_length=50, verbose_name="Abreviación")
  nombre = models.CharField(max_length=100, verbose_name="Nombre")
  color = models.CharField(max_length=20,  verbose_name="Color")

  def __str__(self):
    return self.description

class Unidad(models.Model):
  numero = models.IntegerField(max_length=6, verbose_name="Número Unidad")
  descripcion = models.CharField(max_length=150, verbose_name="Descripcion")
  marca = models.CharField(max_length=100, verbose_name="Marca")
  modelo = models.CharField(max_length=100, verbose_name="Modelo (Año)")
  numero_serie = models.CharField(max_length=100, verbose_name="Número de Serie")
  color = models.CharField(max_length=100, verbose_name="Color")
  activo = models.BooleanField(default=True, verbose_name="Activo")
  numero_choferes = models.IntegerField(max_length=2, default=1, verbose_name="Número de Choferes")
  placas = models.CharField(max_length=20, verbose_name="Placas")
  vencimiento_placas = models.DateField(default=datetime.datetime.today, verbose_name="Fecha de Vencimiento")
  numero_asientos = models.IntegerField(max_length=3, verbose_name="Número de Asientos")
  numero_asientos_x_fila = models.IntegerField(max_length=3, verbose_name="Número de Asientos por Fila")
  numero_filas = models.IntegerField(max_length=3, verbose_name="Número de Filas")
  largo_unidad = models.DecimalField(default=0, decimal_places=2, max_digits=6, verbose_name="Largo (mts)")
  ancho_unidad = models.DecimalField(default=0, decimal_places=2, max_length=6, verbose_name="Acho (mts)")
  alto_unidad = models.DecimalField(default=0, decimal_places=2, max_length=6, verbose_name="Alto (mts)")
  numero_ejes = models.IntegerField(max_length=3, verbose_name="Número de Ejes")
  numero_llantas = models.IntegerField(max_length=3, verbose_name="Número de llantas")
  capacidad_tanque = models.DecimalField(default=0, decimal_places=2, max_length=6, verbose_name="Capacidad Tanque (lts)")
  estatus = models.ForeignKey(Estatus_Unidad, default=1)

  def __str__(self):
    return f'{self.numero} - {self.descripcion}'

class Conductor(models.Model):
  nombre_completo = models.CharField(max_length=250, verbose_name="Nombre Completo")
  imagen = models.ImageField(upload_to="Catalog/Conductor/" , verbose_name="Imagen")
  RFC = models.CharField(max_length=13, verbose_name="RFC")
  CURP = models.CharField(max_length=18, verbose_name="CURP")
  telefono = models.CharField(max_length=20, default="", blank=True)
  licencia = models.CharField(max_length=20, verbose_name="Licencia")
  vencimiento_licencia = models.DateField(default=datetime.datetime.today, verbose_name="Fecha de Vencimiento")
  correo = models.EmailField(max_length=254, verbose_name="Correo Electronico")
  fecha_contratacion = models.DateField(default=datetime.datetime.today, verbose_name="Fecha de Contratación")
  activo = models.BooleanField(default=True, verbose_name="Activo")

  def __str__(self):
    return self.nombre_completo

# class Terminal(models.Model):