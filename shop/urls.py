from django.urls import path
from . import views 
from shop.views import productdetail
from .views import SearchResultsView

urlpatterns = [
    path('', views.product_list,
            name='products'),
    path('search/', SearchResultsView.as_view(),
            name='search_results'),        
    path('<int:category_id>/', views.product_list,
            name='product_list_by_category'),
    path('product/<int:id>/', productdetail, name='productdetail'),
]
