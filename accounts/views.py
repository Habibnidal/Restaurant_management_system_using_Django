from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from accounts.forms import UserForm, UserUpdateForm, UpdateUserProfileform
from accounts.models import userDetails
from venders.models import multiVenders, foodItem, FranchiseRequest


def registration(request):
    registerd = False

    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UpdateUserProfileform(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.set_password(form1.cleaned_data['password'])
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')

    else:
        form1 = UserForm()
        form2 = UpdateUserProfileform()

    return render(request, 'registration.html', {
        'form1': form1,
        'form2': form2,
        'registerd': registerd
    })


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)

            if multiVenders.objects.filter(user=user).exists():
                return redirect('vendor_dashboard')

            if userDetails.objects.filter(user=user).exists():
                return redirect('customer_dashboard')

            return redirect('home')

        return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


@login_required
def home(request):
    venders = multiVenders.objects.filter(is_approved=True)
    return render(request, 'index.html', {'venders': venders})


@login_required
def customer_dashboard(request):
    profile = userDetails.objects.get(user=request.user)
    return render(request, "accounts/customer_dashboard.html", {"profile": profile})


@login_required
def update(request):
    profile = userDetails.objects.get(user=request.user)

    form = UserUpdateForm(instance=request.user)
    form1 = UpdateUserProfileform(instance=profile)

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        form1 = UpdateUserProfileform(request.POST, request.FILES, instance=profile)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('customer_dashboard')

    return render(request, "update.html", {"form": form, "form1": form1})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
