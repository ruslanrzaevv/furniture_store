from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .uttils import q_search
from django.contrib.auth.decorators import login_required

from .models import Products


@login_required
def catalog(request, cat_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if cat_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=cat_slug))

    if on_sale:
        goods = goods.filter(dicount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    caurrent_page = paginator.page(page)

    context = {
        'title': 'Товары',
        'goods': caurrent_page,
        'slug_url': cat_slug       
            
    }   
    return render(request, 'goods/catalog.html', context)


@login_required
def product(request, prod_slug):
    product = Products.objects.get(slug=prod_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
