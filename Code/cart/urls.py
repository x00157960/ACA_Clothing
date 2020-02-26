from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'),
    path('cart/', views.CartPageView.as_view(), name='cart'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
	path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('full_remove/', views.full_remove, name='full_remove'),
]