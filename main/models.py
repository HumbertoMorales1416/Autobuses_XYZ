from django.db import models

class Procesos(models.Model):
  Tipo_Proceso = [
    ('catalogo', 'Catalogo'),
    ('procesos', 'Proceso'),
    ('reportes', 'Reportes'),
    ('configuracion', 'Configuracion'),
  ]

  id_proceso = models.CharField(max_length=7, unique=True, primary_key=True, db_column='id_proceso')
  nombre_proceso = models.CharField(max_length=250)
  descripcion_proceso = models.CharField(max_length=250, verbose_name='Nombre')
  tipo_proceso = models.CharField(max_length=100, choices=Tipo_Proceso, verbose_name='Tipo de Proceso')
  id_proceso_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,  related_name='subproceso', verbose_name='Proceso Principal', db_column='id_proceso_padre')

  class Meta:
    verbose_name_plural = "Procesos"
  
  def __str__(self):
    return f"({self.id_proceso}) - {self.nombre_proceso}"