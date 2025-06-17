from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('afisha', afisha, name='afisha'),
    path('menu', menu, name='menu'),
    path('location', location, name='location'),
    path('contact', contact, name='contact'),
    path('admin_panel', admin_panel, name='admin_panel'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/', views.admin_panel, name='admin_panel'),

    path('admin/drink/edit/<int:drink_id>/', views.edit_drink, name='edit_drink'),
    path('admin/drink/delete/<int:drink_id>/', views.delete_drink, name='delete_drink'),

    path('admin/poster/edit/<int:poster_id>/', views.edit_poster, name='edit_poster'),
    path('admin/poster/delete/<int:poster_id>/', views.delete_poster, name='delete_poster'),
]
