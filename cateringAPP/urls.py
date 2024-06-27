from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index_url' ),
    path('food',views.food,name='food'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('appointments',views.Appointemnt_view,name='appointments'),
    path('packages',views.package_view,name='packages')

]