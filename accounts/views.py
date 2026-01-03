from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.forms import UserForm, UserUpdateForm, UpdateUserProfileform
from accounts.models import userDetails
from venders.models import multiVenders, foodItem, FranchiseRequest


# =========================
# REGISTRATION
# =========================
def registration(request):
    registerd = False

    if request.method == 'POST':
        form1 = UserForm(request.POST)

        if form1.is_valid():
            user = form1.save(commit=False)
            user.set_password(form1.cleaned_data['password'])
            user.save()
            userDetails.objects.create(user=user)
            registerd = True
            return redirect('login')

    else:
        form1 = UserForm()

    return render(request, 'registration.html', {
        'form1': form1,
        'registerd': registerd
    })


# =========================
# LOGIN
# =========================
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            # ROLE CHECK (SAFE)
            if multiVenders.objects.filter(user=user).exists():
                request.session['user_type'] = 'Vender'
                return redirect('vendor_dashboard')

            elif userDetails.objects.filter(user=user).exists():
                request.session['user_type'] = 'Customer'
                return redirect('customer_dashboard')

            else:
                return redirect('/admin/')

        return HttpResponse('<h1>Please check your credentials</h1>')

    return render(request, 'login.html')


# =========================
# HOME
# =========================
@login_required(login_url="login")
def home(request):
    try:
        venders = multiVenders.objects.filter(is_approved=True)
        return render(request, 'index.html', {'venders': venders})
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in home view: {str(e)}")
        messages.error(request, "An error occurred while loading the page.")
        return render(request, 'index.html', {'venders': []})


# =========================
# VENDOR DASHBOARD
# =========================
@login_required(login_url="login")
def vendor_dashboard(request):
    try:
        vendor = multiVenders.objects.get(user=request.user)

        accepted_franchises = FranchiseRequest.objects.filter(
            vendor=vendor,
            status='accepted'
        ).select_related('user')

        return render(request, 'venders/vendor_dashboard.html', {
            'vendor': vendor,
            'fooditems': foodItem.objects.filter(vender=vendor),
            'accepted_franchises': accepted_franchises
        })
    except multiVenders.DoesNotExist:
        messages.error(request, "Vendor profile not found. Please complete your vendor registration.")
        return redirect('home')
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in vendor_dashboard: {str(e)}")
        messages.error(request, "An error occurred. Please try again later.")
        return redirect('home')


# =========================
# CUSTOMER DASHBOARD
# =========================
@login_required(login_url="login")
def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")


# =========================
# UPDATE PROFILE
# =========================
@login_required(login_url="login")
def update(request):
    form = UserUpdateForm(instance=request.user)

    profile, created = userDetails.objects.get_or_create(user=request.user)
    form1 = UpdateUserProfileform(instance=profile)

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        form1 = UpdateUserProfileform(request.POST, request.FILES, instance=profile)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()

            if multiVenders.objects.filter(user=request.user).exists():
                return redirect('vendor_dashboard')
            else:
                return redirect('customer_dashboard')

    return render(request, "update.html", {
        "form": form,
        "form1": form1
    })


# =========================
# LOGOUT
# =========================
@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('login')


# =========================
# FORGOT PASSWORD
# =========================
from django.contrib.auth.models import User

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('forgot_password')

        try:
            user = User.objects.get(username=username)
            user.set_password(password1)
            user.save()
            messages.success(request, "Password changed successfully. Please login.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "User not found")
            return redirect('forgot_password')

    return render(request, 'accounts/forgot_password.html')

