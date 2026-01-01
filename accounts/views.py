from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from venders.models import *

# Create your views here.

def registration(request):
    registerd = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = userFormDetails(request.POST, request.FILES)
        
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            registerd = True
    else:
        form1 = UserForm()
        form2 = userFormDetails()
    return render(request,'registration.html',{'form1':form1,'form2':form2, 'registerd':registerd})

@login_required(login_url="login")
def home(request):
    venders = multiVenders.objects.all()
    return render(request,'index.html',{'venders':venders})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:

                # Assign role based on available related models
                if hasattr(user, 'multivenders'):
                    role = 'Vender'
                elif hasattr(user, 'userdetails'):
                    role = 'Customer'
                else:
                    role = 'Admin'

                request.session['user_type'] = role
                login(request, user)

                # Redirect based on role
                if role == "Vender":
                    return redirect('vendor_dashboard')
                elif role == "Customer":
                    return redirect('customer_dashboard')
                else:
                    return redirect('/admin/')  # Admin goes to Django admin

        return HttpResponse('<h1>Please check your cred....</h1>')
    
    return render(request,'login.html')



@login_required
def vendor_dashboard(request):
    vendor = request.user.multivenders

    accepted_franchises = FranchiseRequest.objects.filter(
        vendor=vendor,
        status='accepted'
    ).select_related('user')

    return render(request, 'venders/vendor_dashboard.html', {
        'vendor': vendor,
        'fooditems': foodItem.objects.filter(vender=vendor),
        'accepted_franchises': accepted_franchises
    })
@login_required(login_url="login")
def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def update(request):
    form = UserUpdateForm(instance=request.user)
    form1=UpdateUserProfileform(instance=request.user.userdetails)
    if request.method=="POST":
        form=UserUpdateForm(request.POST,request.FILES,instance=request.user)
        form1=UpdateUserProfileform(request.POST,request.FILES,instance=request.user.userdetails)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            profile=form1.save(commit=False)
            profile.user=user
            profile.save()

            # Redirect based on user type
            if hasattr(user, 'multivenders'):
                return redirect('vendor_dashboard')
            elif hasattr(user, 'userdetails'):
                return redirect('customer_dashboard')
            else:
                return redirect('/admin/')
    return render(request,"update.html",{"form":form,"form1":form1})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

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

    
    
