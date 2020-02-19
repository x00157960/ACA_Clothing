from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'),
    path('cart/', views.CartPageView.as_view(), name='cart'),
]