from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
            })

       }




