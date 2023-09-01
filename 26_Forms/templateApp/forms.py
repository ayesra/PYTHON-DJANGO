from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

        labels={
            'first_name':'Adınızı girniz',
            'gender':'cinsiyet seçiniz',

        }
        widgets={
            'gender':forms.RadioSelect
        }


