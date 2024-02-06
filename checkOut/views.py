from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart,CartItem
from account.models import Account
from django.contrib import messages
from decimal import Decimal, ROUND_HALF_UP
from django.contrib.sessions.models import Session

# Create your views here.
def checkout_page(request):

    user_id = request.user.id if request.user.is_authenticated else None
    session_id = request.session.session_key

    if not user_id:
        cart,created_cart = Cart.objects.get_or_create(session_key=session_id)
    else:
        user_instance = get_object_or_404(Account,id=user_id)
        cart,created_cart = Cart.objects.get_or_create(user=user_instance,session_key=session_id)



    if request.method=="POST":
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity',1))

        cart_item = get_object_or_404(CartItem,id=cart_item_id)

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart.items.remove(cart_item)
            cart_item.delete()

    cart.refresh_from_db()

    total_price = Decimal('0.0')
    for cart_item in cart.items.all():
        item_price = Decimal(cart_item.product.product_price)
        item_quantity = Decimal(cart_item.quantity)
        item_total_price = (item_price*item_quantity).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
        total_price += item_total_price
        cart_item.total_price = item_total_price

    total_price = total_price.quantize(Decimal('0.0'),rounding=ROUND_HALF_UP)


    tax_percentage = Decimal('0.18')
    tax = (tax_percentage*total_price).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)


    grand_total = (total_price+tax).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

    context = {
        'cart_items':cart.items.all(),
        'total_price':total_price,
        'each_price':cart_item.product.product_price,
        'tax':tax,
        'grand_total':grand_total
    }

    return render(request,"place-order.html",context)