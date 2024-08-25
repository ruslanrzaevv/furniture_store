from django.urls import path, include
from app.settings import DEBUG


from goods import views


urlpatterns = [
    path('search/', views.catalog, name='search'),

    path('catalog/<slug:cat_slug>/', views.catalog, name='catalog'),
    path('product/<slug:prod_slug>/', views.product, name='product'), 
]




if DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]