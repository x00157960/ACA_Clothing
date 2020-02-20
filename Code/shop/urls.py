from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('browse/', ProductListView.as_view(),
                name='browse'),
]