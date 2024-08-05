from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from cateringAPP.models import *
from .forms import *
from django.urls import reverse
# Core Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Avg, Count, Q
from datetime import datetime


# Decorators
from django.contrib.admin.views.decorators import staff_member_required


# Authentication
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Messaging
from django.contrib import messages

# Email handling
from django.core.mail import send_mail
from django.template.loader import render_to_string

# URL handling and encoding
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

# Local app imports
from .models import *
from .forms import *
# ACCOUNT


# Sign Up

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index_url")

            messages.success(request, "Your Account has been created successfully!")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


# Sign In

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index_url")
        else:
            if not request.POST.get("username") or not request.POST.get("password"):
                # No message will be displayed for empty fields
                pass
            else:
                # Display error message for invalid username or password
                messages.error(request, ("Invalid username or password."))
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {"form": form})

# Sign Out
def signout_view(request):
    logout(request)
    return redirect("index_url")

# Profile
def profile_view(request):
    profileIcon = Customer.objects.all()
    customer = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get("new_password")
            if new_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
            user.save()

            # Ensure the Customer email is updated to match the User email
            customer = request.user.customer
            customer.email = user.email
            customer.save()

            messages.success(request, "Your profile has been updated successfully!")
            return redirect("Account:profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(
        request,
        "profile.html",
        {
            "form": form,
            "customer": request.user.customer,
            "customer": customer,
            "profileIcon": profileIcon,
        },
    )


# Delete Profile

def delete_profile_view(request):
    if request.method == "POST":
        form = ProfileDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirm"]:
            user = request.user
            customer = user.customer
            customer.delete()  # Delete the related customer profile
            user.delete()  # Delete the user account
            logout(request)
            messages.success(request, "Your profile has been deleted successfully.")
            return redirect("signin")
    else:
        form = ProfileDeleteForm()
    return render(request, "delete_profile.html", {"form": form})


# Reset Password

def password_reset_request(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "user/account/password_reset_email.html"
                    context = {
                        "email": user.email,
                        "domain": request.META["HTTP_HOST"],
                        "site_name": "Your Site",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, context)
                    send_mail(
                        subject,
                        email,
                        "admin@yourdomain.com",
                        [user.email],
                        fail_silently=False,
                    )
                return redirect("password_reset_done")
    else:
        form = CustomPasswordResetForm()
    return render(request, "password_reset.html", {"form": form})


# Reset Password Done
def password_reset_done(request):
    return render(request, "password_reset_done.html")


# Password Reset Confirm
def password_reset_confirm(request, uidb64=None, token=None):
    UserModel = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = CustomSetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect("password_reset_complete")
        else:
            form = CustomSetPasswordForm(user)
        return render(
            request, "password_reset_confirm.html", {"form": form}
        )
    else:
        return render(request, "password_reset_invalid.html")


# Password Reset Complete

def password_reset_complete(request):
    return render(request, "password_reset_complete.html")
