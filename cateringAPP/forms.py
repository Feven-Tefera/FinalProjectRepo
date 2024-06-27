from django.shortcuts import render, redirect
from django import forms
from .models import *


class packageform(forms.Form):
    package_name=forms.CharField(max_length=100)
    packimg=forms.ImageField()
    package_price=forms.DecimalField(max_digits=10, decimal_places=2)
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package_name', 'packimg', 'package_price']
        widgets = {
            'package_name': forms.TextInput(attrs={'class': 'form-control'}),
            'packimg': forms.FileInput(attrs={'class': 'form-control-file'}),
            'package_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def str(self) -> str:
            return self.package_name