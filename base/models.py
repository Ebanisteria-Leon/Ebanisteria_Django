from django.db import models

from simple_history.models import HistoricalRecords

# Create your models here.

#* Modelo base
class BaseModel(models.Model):
    estadoCreacion = models.BooleanField(
        verbose_name = 'Estado de Creacion', default = True)
    fechaCreacion = models.DateField(
        verbose_name = 'Fecha de Creacion', auto_now = False, auto_now_add = True)
    fechaModificacion = models.DateField(
        verbose_name = 'Fecha de Modificacion', auto_now = False, auto_now_add = True)
    fechaEliminacion = models.DateField(
        verbose_name = 'Fecha de Eliminacion', auto_now = False, auto_now_add = True)
    historical = HistoricalRecords(user_model = "users.User", inherit = True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = 'Modelo base'
        verbose_name_plural = 'Modelos base'
