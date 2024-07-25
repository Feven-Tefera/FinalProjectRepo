from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'Account'

urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]