from apiTechnicalSpecification.models import Equipment
from django.forms import ModelForm, TextInput, Textarea


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['equipment_type', 'serial_number', 'note']

        widgets = {
            "serial_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серийный номер'
            }),
            "note": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Примечание'
            })
        }
