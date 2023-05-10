from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.productdetails, name='productdetails'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('editproducts/<int:product_id>/',
         views.editproducts, name='editproducts'),
    path('deleteproducts/<int:product_id>/',
         views.deleteproducts, name='deleteproducts'),
]
