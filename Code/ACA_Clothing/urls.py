from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/create/', views.SignupView, name='signup'),
    path('account/login/', views.SigninView, name='signin'),
    path('account/logout/', views.SignoutView, name='signout'),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('search/', include('search_app.urls')),
    path('', include('pages.urls'), name='home'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)