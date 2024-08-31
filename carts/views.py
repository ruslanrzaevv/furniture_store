from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from goods.models import Products
from carts.models import Cart
from carts.utils import get_user_carts


def cart_add(request):
    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)
        
        if cart.exists():
            cart = cart.first()

            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product,quantity=1)  
    
    user_cart = get_user_carts(request)
    cart_items_html: str = render_to_string(
    "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


    return JsonResponse(response_data)

def cart_change(request):
    ...

def cart_remove(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


















