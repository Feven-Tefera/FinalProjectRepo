from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_url' ),
    path('food/',views.food,name='food'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('appointments',views.Appointemnt_view,name='appointments'),
    path('packages',views.package_view,name='packages'),
    path('tables',views.tables_view,name='tables'),
    path('package-edit/<int:pk>/', views.package_edit_view, name='package_edit_view'),
    path('package-delete/<int:pk>/', views.package_delete_view, name='package_delete_view'),
    path('menucategory',views.menu_cat_view,name='menucategory'),
    path('menus',views.menu_view,name='menus'),
    path('cart',views.cart_view,name='cart'),

]