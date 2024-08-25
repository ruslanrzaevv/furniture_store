from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'), 
    path('registr/', views.registration, name='registr'), 
    path('users-cart', views.users_cart, name='users_cart'),
    path('logout/', views.logout, name='logout'), 
]
