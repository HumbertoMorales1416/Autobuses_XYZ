import os
import imghdr
import datetime
import unicodedata
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Sanitizar el nombre del archivo (sin caracteres extraños)
def sanitize_filename(filename):
    return ''.join(
        c for c in unicodedata.normalize('NFD', filename)
        if unicodedata.category(c) != 'Mn'
    )

# Renombra el archivo con formato: nombre_fecha.ext
def custom_upload_logo_to(instance, filename):
    sanitized_name = sanitize_filename(instance.nombre.replace(" ", "_"))
    extension = os.path.splitext(filename)[-1].lower()
    new_filename = f"{sanitized_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}{extension}"
    return f'catalogo/lineas/{new_filename}'

# Validar tipo de archivo (MIME type)
def validate_image_mime(file):
    valid_mime_types = ['jpg', 'jpeg', 'png']
    file_mime_type = imghdr.what(file)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('El archivo no es una imagen válida.')

# Clase que se utiliza para saber los estatus que se pueden colocar a una unidad (Disponible, En transito, En Mantenimiento, etc)    
class Estatus_Unidad(models.Model):
  abreviacion = models.CharField(max_length=50, verbose_name="Abreviación")
  nombre = models.CharField(max_length=100, verbose_name="Nombre")
  color = models.CharField(max_length=7, validators=[RegexValidator(
          regex=r'^#(?:[0-9a-fA-F]{3}){1,2}$', 
          message='El color debe estar en formato HEX, por ejemplo: #RRGGBB'
      )], verbose_name="Color")

  def __str__(self):
    return f'{self.abreviacion} - {self.nombre}'

  class Meta:
    verbose_name_plural = "Estatus de unidades"
    permissions = [
            ('can_view_estatus_unidad', 'Estatus de Unidades'),
            ('can_add_estatus_unidad', 'Agregar'),
            ('can_edit_estatus_unidad', 'Modificar'),
            ('can_delete_estatus_unidad', 'Eliminar'),
        ]
  
# Clase para poder dar de alta las lineas comerciales de los autobuses
class Lineas_Unidades(models.Model):
  nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
  logo = models.ImageField(upload_to=custom_upload_logo_to, validators=[validate_image_mime], null=True, blank=True, verbose_name="Logo")

  def __str__(self):
    return self.nombre
  
  class Meta:
    verbose_name_plural = "Lineas"
    permissions = [
            ('can_view_lineas_unidad', 'Lineas'),
            ('can_add_lineas_unidad', 'Agregar'),
            ('can_edit_lineas_unidad', 'Modificar'),
            ('can_delete_lineas_unidad', 'Eliminar'),
        ]

# class Unidad(models.Model):
#   numero = models.IntegerField(verbose_name="Número Unidad")
#   linea = models.ForeignKey(Lineas_Unidades, on_delete=models.DO_NOTHING, default=1, verbose_name="Linea")
#   marca = models.CharField(max_length=100, verbose_name="Marca")
#   modelo = models.CharField(max_length=100, verbose_name="Modelo (Año)")
#   numero_serie = models.CharField(max_length=100, verbose_name="Número de Serie")
#   color = models.CharField(max_length=100, verbose_name="Color")
#   activo = models.BooleanField(default=True, verbose_name="Activo")
#   numero_choferes = models.IntegerField(default=1, verbose_name="Número de Choferes")
#   placas = models.CharField(max_length=20, verbose_name="Placas")
#   vencimiento_placas = models.DateField(default=datetime.datetime.today, verbose_name="Fecha de Vencimiento")
#   numero_asientos = models.IntegerField(verbose_name="Número de Asientos")
#   numero_asientos_x_fila = models.IntegerField(verbose_name="Número de Asientos por Fila")
#   numero_filas = models.IntegerField(verbose_name="Número de Filas")
#   largo_unidad = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Largo (mts)")
#   ancho_unidad = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Acho (mts)")
#   alto_unidad = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Alto (mts)")
#   numero_ejes = models.IntegerField(verbose_name="Número de Ejes")
#   numero_llantas = models.IntegerField(verbose_name="Número de llantas")
#   capacidad_tanque = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Capacidad Tanque (lts)")
#   estatus = models.ForeignKey(Estatus_Unidad, on_delete=models.DO_NOTHING, default=1, verbose_name="Estatus")

#   def __str__(self):
#     return f'{self.numero} - {self.linea.nombre}'

# class Conductor(models.Model):
#   nombre_completo = models.CharField(max_length=250, verbose_name="Nombre Completo")
#   imagen = models.ImageField(upload_to="Catalogo/Conductor/", verbose_name="Imagen")
#   RFC = models.CharField(max_length=13, verbose_name="RFC")
#   CURP = models.CharField(max_length=18, verbose_name="CURP")   
#   telefono = models.CharField(max_length=20, default="", blank=True)
#   licencia = models.CharField(max_length=20, verbose_name="Licencia")
#   vencimiento_licencia = models.DateField(default=datetime.datetime.today, verbose_name="Fecha de Vencimiento")
#   correo = models.EmailField(max_length=254, verbose_name="Correo Electronico")
#   fecha_contratacion = models.DateField(default=datetime.datetime.today, verbose_name="Fecha de Contratación")
#   activo = models.BooleanField(default=True, verbose_name="Activo")
#   observaciones = models.CharField(max_length=500, default='', blank=True, null=True, verbose_name="Observaciones")

#   def __str__(self):
#     return self.nombre_completo

# class Terminal(models.Model):