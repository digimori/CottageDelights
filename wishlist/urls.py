from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('addwish/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('adjustwish/<item_id>/', views.adjust_wishlist, name='adjust_wishlist'),
    path('removewish/<item_id>/',
         views.remove_from_wishlist, name='remove_from_wislist'),
]
