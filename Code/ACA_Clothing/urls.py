from django.contrib import admin
from django.urls import path, include
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/create/', views.SignupView, name='signup'),
    path('account/login/', views.SigninView, name='signin'),
    path('account/logout/', views.SignoutView, name='signout'),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
]
