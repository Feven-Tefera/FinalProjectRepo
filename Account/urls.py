from django.urls import path
from . import views
app_name = 'Account'
urlpatterns = [
 path("Sign-In", views.signin_view, name="signin"),
 path("Sign-Up", views.signup_view, name="signup"),
 path("Sign-Out", views.signout_view, name="signout"),   
 # Authentication views
    # Profile views
    path("Profile", views.profile_view, name="profile"),
    path("Profile/Delete", views.delete_profile_view, name="delete_profile"),
    # Password reset views
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        views.password_reset_confirm,
        name="password_reset_confirm",
    ),
    path("password_reset/done/", views.password_reset_done, name="password_reset_done"),
    path("reset/done/", views.password_reset_complete, name="password_reset_complete"),
]