from django.urls import path
from carts import views


urlpatterns = [
    path('cart_add/<slug:prod_slug>/', views.cart_add, name='cart_add'),
    path('cart_change/<slug:prod_slug>/', views.cart_change, name='cart_change'), 
    path('cart_remove/<slug:prod_slug>', views.cart_remove, name='cart_remove'),
]
    