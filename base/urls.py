from django.urls import path
from . import views

urlpatterns = [
    path('', views.default),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('login/', views.loginPage, name='login'),
    path('product/', views.product, name='product')
]
