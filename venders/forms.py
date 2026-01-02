from django import forms
from django.contrib.auth import get_user_model
from venders.models import multiVenders, foodItem

User = get_user_model()


# -------------------------
# Vendor User Registration
# -------------------------
class venderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# -------------------------
# Vendor Details Form
# -------------------------
class venderDetailsForm(forms.ModelForm):
    class Meta:
        model = multiVenders
        fields = [
            'restaurent_name',
            'address',
            'city',
            'state',
            'zipcode',
            'restaurent_img',
            'restaurent_lic',
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }


# -------------------------
# Add Food Form
# -------------------------
class addFoodForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = [
            'food_name',
            'food_desc',
            'price',
            'food_img',
        ]


# -------------------------
# Edit Food Form
# -------------------------
class FoodEditForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = [
            'food_name',
            'food_desc',
            'price',
            'food_img',
        ]
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control'}),
            'food_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'food_img': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_food_name(self):
        food_name = self.cleaned_data.get('food_name')
        if not food_name:
            raise forms.ValidationError("Food name is required.")
        return food_name
