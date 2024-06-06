from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'Account'

urlpatterns=[
    path('Login',views.login_view, name='Login'),
    path('signup',views.signup_view,name='signup'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)