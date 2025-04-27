# dogs/forms.py
from django import forms
from .models import Dog, Pedigree
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'description', 'image', 'birth_date']  # Укажите поля, которые нужно отображать в форме
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),  # Для удобного выбора даты
        }

PedigreeFormSet = inlineformset_factory(Dog, Pedigree, fields=('father', 'mother', 'grand_father_father', 'grand_mother_father', 'grand_father_mother', 'grand_mother_mother'), extra=1, can_delete=True)