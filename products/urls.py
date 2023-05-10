from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.productdetails, name='productdetails'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('edit/<int:product_id>/', views.editproduct, name='editproduct'),
]
