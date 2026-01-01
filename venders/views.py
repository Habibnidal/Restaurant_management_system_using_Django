from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import multiVenders, foodItem, FranchiseRequest
from .forms import venderForm, venderDetailsForm, addFoodForm, FoodEditForm

def venderRegister(request):
    registerd = False

    if request.method == 'POST':
        user_form = venderForm(request.POST)
        details_form = venderDetailsForm(request.POST, request.FILES)

        if user_form.is_valid() and details_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            details = details_form.save(commit=False)
            details.user = user
            details.save()
            registerd = True
            messages.success(request, 'Vendor registered successfully!')
            return redirect('login')
    else:
        user_form = venderForm()
        details_form = venderDetailsForm()
    
    return render(request, 'venders/vender_register.html', {
        'form1': user_form,
        'form2': details_form, 
        'registerd': registerd
    })

def vender_details(request, id):
    vender = get_object_or_404(multiVenders, id=id)
    fooditems = foodItem.objects.filter(vender=id)
    
    user_has_pending_request = False
    if request.user.is_authenticated:
        user_has_pending_request = FranchiseRequest.objects.filter(
            vendor=vender,
            user=request.user,
            status='pending'
        ).exists()
    
    return render(request, 'venders/vender_details.html', {
        'vender': vender,
        'fooditems': fooditems,
        'user_has_pending_request': user_has_pending_request,
    })

@login_required
def addFood(request):
    if not hasattr(request.user, 'multivenders'):
        raise PermissionDenied("Only vendors can add food items.")

    if request.method == "POST":
        form = addFoodForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.vender = request.user.multivenders
            item.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('vendor_dashboard')
    else:
        form = addFoodForm()
    
    return render(request, 'venders/addfood.html', {'form': form})

@login_required
def food_edit(request, id):
    try:
        food_item = get_object_or_404(foodItem, id=id)
        
        if request.user != food_item.vender.user:
            raise PermissionDenied("You don't have permission to edit this item.")
        
        if request.method == 'POST':
            form = FoodEditForm(request.POST, request.FILES, instance=food_item)
            if form.is_valid():
                form.save()
                messages.success(request, 'Food item updated successfully!')
                return redirect('vendor_dashboard')
        else:
            form = FoodEditForm(instance=food_item)
            
        return render(request, 'venders/foodedit.html', {
            'form': form,
            'food_item': food_item
        })
        
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('vendor_dashboard')

@login_required
def food_delete(request, id):
    try:
        food_item = get_object_or_404(foodItem, id=id)
        
        if request.user != food_item.vender.user:
            raise PermissionDenied("You don't have permission to delete this item.")
        
        if request.method == 'POST':
            food_item.delete()
            messages.success(request, 'Food item deleted successfully!')
        
        return redirect('vendor_dashboard')
            
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('vendor_dashboard')

@login_required
def request_franchise(request, vendor_id):
    vendor = get_object_or_404(multiVenders, id=vendor_id)
    
    if not vendor.is_franchise_available:
        messages.error(request, "Franchise is not available for this restaurant.")
        return redirect('venders:venderdetails', id=vendor_id)
    
    existing_request = FranchiseRequest.objects.filter(
        vendor=vendor,
        user=request.user,
        status='pending'
    ).exists()
    
    if existing_request:
        messages.info(request, "You already have a pending franchise request for this restaurant.")
        return redirect('venders:venderdetails', id=vendor_id)
    
    FranchiseRequest.objects.create(
        vendor=vendor,
        user=request.user,
        status='pending'
    )
    
    messages.success(request, "Your franchise request has been submitted successfully!")
    return redirect('venders:venderdetails', id=vendor_id)

@login_required
def edit_vendor(request, id):
    vendor = get_object_or_404(multiVenders, id=id)
    
    if request.user != vendor.user:
        raise PermissionDenied("You don't have permission to edit this vendor profile.")
    
    if request.method == 'POST':
        form = venderDetailsForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor details updated successfully!')
            return redirect('venders:venderdetails', id=id)
    else:
        form = venderDetailsForm(instance=vendor)
    
    return render(request, 'venders/edit_vendor.html', {
        'form': form,
        'vender': vendor
    })

@login_required
def franchise_details(request, vendor_id):
    vendor = get_object_or_404(multiVenders, id=vendor_id, is_franchise_available=True)
    
    if request.method == 'POST' and 'accept_franchise' in request.POST:
        franchise_request, created = FranchiseRequest.objects.get_or_create(
            user=request.user,
            vendor=vendor,
            defaults={'status': 'pending'}
        )
        if created:
            messages.success(request, 'Your franchise request has been submitted for review.')
        else:
            messages.info(request, 'You have already submitted a request for this franchise.')
        return redirect('venders:franchise_details', vendor_id=vendor_id)
    
    context = {
        'vendor': vendor,
        'user_has_pending_request': FranchiseRequest.objects.filter(
            user=request.user,
            vendor=vendor,
            status='pending'
        ).exists()
    }
    return render(request, 'venders/franchise_details.html', context)

@login_required
def franchise_requests(request):
    if not hasattr(request.user, 'multivenders'):
        messages.error(request, "Only vendors can view franchise requests.")
        return redirect('home')
        
    vendor = request.user.multivenders
    requests = FranchiseRequest.objects.filter(vendor=vendor).order_by('-created_at')
    
    return render(request, 'venders/franchise_requests.html', {
        'requests': requests
    })
@login_required
def accepted_franchises(request):
    if not hasattr(request.user, 'multivenders'):
        messages.error(request, "Only vendors can view accepted franchises.")
        return redirect('home')

    vendor = request.user.multivenders

    accepted_requests = FranchiseRequest.objects.filter(
        vendor=vendor,
        status='accepted'
    )

    return render(request, 'venders/accepted_franchises.html', {
        'accepted_requests': accepted_requests
    })

