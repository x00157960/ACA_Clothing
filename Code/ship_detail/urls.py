from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShipPageView.as_view(), name='ship'),

]