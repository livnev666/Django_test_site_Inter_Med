from django.db import models
from django.urls import reverse

# Create your models here.
class Modalities(models.Model):
    short_code = models.CharField(max_length=10, verbose_name='Короткий код')
    name = models.CharField(max_length=250, verbose_name='Наименование модальности')


class Studies(models.Model):
    patient_fio = models.CharField(max_length=250, verbose_name='ФИО пациента')
    patient_birthdate = models.DateField(blank=True, null=True, verbose_name='Дата рождения пациента')
    study_uid = models.UUIDField(verbose_name='Идентификатор исследования во внешней системе')
    study_date = models.DateTimeField(verbose_name='Дата и время исследования')
    study_modality = models.ForeignKey(Modalities, on_delete=models.DO_NOTHING, verbose_name='Модальность исследования')

    class Meta:
        ordering = ['patient_fio', 'patient_birthdate', 'study_uid', 'study_date', 'study_modality']