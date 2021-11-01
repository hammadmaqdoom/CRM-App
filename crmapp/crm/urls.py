from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('quotations/', views.usersignup, name='quotations'),
    path('invoices/', views.usersignup, name='invoices'),
    path('purchases/', views.purchases, name='purchases'),
    path('productservices/', views.productservices, name='productservices'),
]
