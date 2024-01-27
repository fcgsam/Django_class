from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,CartItem
from ClothApp.models import ProductModel
from account.models import Account
from django.contrib import messages

# Create your views here.

def add_to_cart(request,id):
    items = get_object_or_404(ProductModel,id = id)

    user_id = request.user_id if request.user.is_authenticated else None
    session_id = request.session.session_key

    if not session_id:
        request.session.save()
        session_id = request.session.session_key


    cart_item,created = CartItem.objects.get_or_create(user_id = user_id,product = items)

    if not user_id:
        cart,created_cart = Cart.objects.get_or_create(session_key = session_id)
        cart.items.add(cart_item)
    else:
        user_instance = Account.objects.get(id = user_id)
        cart , created_cart = Cart.objects.get_or_create(user = user_instance,session_key = session_id)
        cart.items.add(cart_item)

    if request.method =='POST':
        quantity = int(request.POST.get('quentity'),1)
        if created:
            cart_item.quentity = quantity
        else:
            cart_item.quentity +=quantity

        cart_item.save()

    if not user_id:
        total_items_count = Cart.objects.get(session_key = session_id).items.count()

    else:
        total_items_count = sum(cart.items.all().count() for cart in request.user.cart.all())

    messages.success(request,f"{items.product_name} Added to cart successfully")
    request.session['total_item_count'] = total_items_count
    return redirect('home')
    