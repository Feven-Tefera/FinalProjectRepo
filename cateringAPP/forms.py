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
    
class menucatform(forms.Form):
    category_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    menu_categories_pack = forms.ModelChoiceField(queryset=Package.objects.all(), to_field_name='id', label='Package', widget=forms.Select(attrs={'class': 'form-control'}))
class Menucatform(forms.ModelForm):
     class Meta:
          model=MenuCategory
          fields ="__all__"
          widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category_description': forms.Textarea(attrs={'class': 'form-control-file'}),
            'menu_categories_pack': forms.TextInput(attrs={'class': 'form-control'}),
        }

     def str(self) ->str:
             return self.category_name
     
class menuForm(forms.ModelForm):
    item_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    item_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    item_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    category = forms.ModelChoiceField(queryset=MenuCategory.objects.all(), to_field_name='id', label='MenuCategory', widget=forms.Select(attrs={'class': 'form-control'}))
    packages = forms.ModelChoiceField(queryset=Package.objects.all(), to_field_name='id', label='Package', widget=forms.Select(attrs={'class': 'form-control'}))
    # created_at = forms.DateTimeField(widget=forms.HiddenInput())
    # updated_at = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = MenuItem
        fields = "__all__"
        extra_kwargs = {
            'created_at': {'auto_now_add': True},
            'updated_at': {'auto_now': True},
        }

    def __str__(self):
        return self.item_name

   