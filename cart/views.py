from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Cart, CartItem
from venders.models import foodItem
from django.conf import settings
from decimal import Decimal

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.select_related('food_item', 'food_item__vender').all()
        subtotal = sum(item.total_price for item in cart_items)
        delivery_fee = Decimal('50.00')
        tax_rate = Decimal('0.05')  # 5% GST
        tax = subtotal * tax_rate
        total = subtotal + tax + delivery_fee
        
        return render(request, 'cart/cart.html', {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'tax': tax,
            'delivery_fee': delivery_fee,
            'total': total,
        })
    except Cart.DoesNotExist:
        return render(request, 'cart/cart.html', {
            'cart_items': [],
            'subtotal': 0,
            'tax': 0,
            'delivery_fee': 0,
            'total': 0,
        })
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in view_cart: {str(e)}")
        messages.error(request, "An error occurred while loading your cart.")
        return render(request, 'cart/cart.html', {
            'cart_items': [],
            'subtotal': 0,
            'tax': 0,
            'delivery_fee': 0,
            'total': 0,
        })

from django.http import JsonResponse

@login_required
@require_POST
def add_to_cart(request, food_item_id):
    try:
        food_item = foodItem.objects.get(id=food_item_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity < 1:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Quantity must be at least 1.'}, status=400)
            messages.error(request, "Quantity must be at least 1.")
            return redirect('venders:food_items')
            
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Check if item already in cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            food_item=food_item,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f"{quantity} x {food_item.food_name} added to your cart!",
                'cart_count': cart.items.count()
            })
        else:
            messages.success(request, f"{quantity} x {food_item.food_name} added to your cart!")
            return redirect('cart:view_cart')
            
    except (ValueError, foodItem.DoesNotExist) as e:
        error_msg = "Error adding item to cart. Please try again."
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'error': error_msg}, status=400)
        messages.error(request, error_msg)
        return redirect('venders:food_items')

@login_required
def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        food_name = cart_item.food_item.food_name
        cart_item.delete()
        messages.success(request, f"{food_name} removed from your cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "Item not found in your cart.")
    
    return redirect('cart:view_cart')

@login_required
@require_POST
def update_cart_item(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity < 1:
            cart_item.delete()
            messages.success(request, "Item removed from your cart.")
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Cart updated successfully!")
            
    except (ValueError, CartItem.DoesNotExist):
        messages.error(request, "Error updating cart. Please try again.")
    
    return redirect('cart:view_cart')

@login_required
def increment_cart_item(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Quantity increased.")
    except CartItem.DoesNotExist:
        messages.error(request, "Item not found in your cart.")
    return redirect('cart:view_cart')

@login_required
def decrement_cart_item(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, "Quantity decreased.")
        else:
            messages.info(request, "Quantity cannot be less than 1. Use remove to delete the item.")
    except CartItem.DoesNotExist:
        messages.error(request, "Item not found in your cart.")
    return redirect('cart:view_cart')
@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.select_related('food_item', 'food_item__vender').all()
        cart_total = sum(item.total_price for item in cart_items)
        delivery_fee = Decimal('50.00')  # Delivery fee
        tax_rate = Decimal('0.05')  # 5% GST
        tax = cart_total * tax_rate
        # Total = Subtotal + Tax + Delivery Fee
        total = cart_total + tax + delivery_fee
        
        context = {
            'cart_items': cart_items,
            'cart_total': cart_total,
            'cart_tax': tax,
            'delivery_fee': delivery_fee,
            'cart_total_with_tax': total,
        }
        return render(request, 'cart/payment.html', context)
    except Cart.DoesNotExist:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart:view_cart')
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in checkout: {str(e)}")
        messages.error(request, "An error occurred during checkout.")
        return redirect('cart:view_cart')

