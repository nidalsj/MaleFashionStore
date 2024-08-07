from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderedItem, Coupon
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product

# Create your views here.


def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    
    if request.method == "POST":
        coupon_code = request.POST.get('code')
        total_amount = float(request.POST.get('total', 0))  # Retrieve total from hidden input
        print(coupon_code)
        # try:
        #     coupon = Coupon.objects.get(coupon_code=coupon_code, is_expired=False)
        #     if total_amount >= coupon.minimum_amount:
        #         cart_obj.coupon = coupon
        #         cart_obj.total_price = total_amount - coupon.discount_amount  
        #         cart_obj.save()
        #         messages.success(request, 'Coupon applied successfully!')
        #     else:
        #         messages.error(request, f'Minimum cart amount should be ₹{coupon.minimum_amount} to apply this coupon.')
        # except Coupon.DoesNotExist:
        #     messages.error(request, 'Invalid coupon code or coupon has expired.')

    context={'cart':cart_obj}
    return render(request, "cart.html", context)


@login_required(login_url="user_login")
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get("quantity"))
        size = request.POST.get("size")
        product_id = request.POST.get("product_id")
        cart_obj, created = Order.objects.get_or_create(
            owner=customer, order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            size=size,
            owner=cart_obj,
        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity + quantity
            ordered_item.save()
        return redirect("cart")


def remove_item_from_cart(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')


def checkout(request):
    return render(request, 'checkout.html')