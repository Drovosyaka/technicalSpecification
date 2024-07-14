from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
import re

from rest_framework.exceptions import ValidationError


class EquipmentType(models.Model):
    code = models.AutoField(primary_key=True)
    title = models.CharField(_('Наименование оборудования'), max_length=255)
    serial_number_mask = models.CharField(_('Маска'), max_length=20, blank=True, default='', unique=True)

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

    def clean(self):
        validate_serial_number(self.serial_number, self.equipment_type.serial_number_mask)
        if Equipment.objects.filter(serial_number=self.serial_number).exists():
            raise ValidationError(f'Серийный номер {self.serial_number} уже существует.')

    def get_absolute_url(self):
        return f'/search/{self.code}/update/'

    class Meta:
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудования')

    def __str__(self):
        return f'{self.equipment_type}:{self.serial_number}'


def validate_serial_number(value, serial_number_mask):
    regex = pattern_to_regex(serial_number_mask)
    if not re.fullmatch(regex, value):
        raise ValidationError(f'{value} не соответствует шаблону: {serial_number_mask}')


def pattern_to_regex(serial_number_mask):
    mapping = {
        'N': r'\d',
        'A': r'[A-Z]',
        'a': r'[a-z]',
        'X': r'[A-Z0-9]',
        'Z': r'[-_@]'
    }
    regex = ''.join(mapping.get(char, char) for char in serial_number_mask)
    return regex