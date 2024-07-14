from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
import re

from rest_framework.exceptions import ValidationError


class EquipmentType(models.Model):
    code = models.AutoField(primary_key=True)
    title = models.CharField(_('Маска'), max_length=255)
    serial_number_mask = models.CharField(max_length=20, blank=True, default='')

    # def clean_serial_number_mask(self):
    #     """Проверка корректности маски серийного номера."""
    #     if not self.serial_number_mask:
    #         raise ValidationError('Маска серийного номера должна быть задана.')
    #     if not re.match(r'^[Nn][Aa][Xx]+$', self.serial_number_mask):
    #         raise ValidationError(
    #             'Маска серийного номера не соответствует формату.')
    #     return self.serial_number_mask
    #
    # def save(self, *args, **kwargs):
    #     self.clean_serial_number_mask()
    #     super().save(*args, **kwargs)
    #
    class Meta:
        verbose_name = _('Тип Оборудования')
        verbose_name_plural = _('Тип Оборудования')

    def __str__(self):
        return self.title


class Equipment(models.Model):
    code = models.AutoField(primary_key=True)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^[0-9A-Za-zX-Z-_@]+$', message='Серийный номер не соответствует маске.')])
    note = models.TextField()

    def get_absolute_url(self):
        return f'/search/{self.code}/update/'

    class Meta:
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудования')

    def __str__(self):
        return f'{self.equipment_type}:{self.serial_number}'
