from django import forms
from cateringAPP.models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


# User registration form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=80, required=True)
    subcity = forms.CharField(max_length=80, required=True)
    phonenum = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "firstname",
            "lastname",
            "city",
            "subcity",
            "phonenum",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            customer = Customer(
                user=user,
                firstname=self.cleaned_data["firstname"],
                lastname=self.cleaned_data["lastname"],
                email=self.cleaned_data["email"],
                city=self.cleaned_data["city"],
                subcity=self.cleaned_data["subcity"],
                phonenum=self.cleaned_data["phonenum"],
            )
            customer.save()
        return user

# Profile update form
class ProfileUpdateForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ["email"]

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            raise forms.ValidationError(
                "New password and confirm password do not match."
            )

        return cleaned_data


# Profile delete form
class ProfileDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="I confirm that I want to delete my profile.")


# Custom password reset form
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)


# Custom set password form
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(
        label="New password confirmation", widget=forms.PasswordInput
    )
