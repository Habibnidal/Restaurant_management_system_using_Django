from django import forms
from venders.models import multiVenders, foodItem
from django.contrib.auth import get_user_model


User = get_user_model()


class venderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

class venderDetailsForm(forms.ModelForm):
    class Meta:
        model = multiVenders
        fields = '__all__'
        exclude = ('is_approved', 'user_type', 'user')

class addFoodForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = '__all__'
        exclude = ('vender',)

class FoodEditForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = ['food_name', 'food_desc', 'price', 'food_img']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control'}),
            'food_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'food_img': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'food_name': 'Food Name',
            'food_desc': 'Description',
            'price': 'Price',
            'food_img': 'Food Image'
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
    # In venders/forms.py
class venderDetailsForm(forms.ModelForm):
    class Meta:
        model = multiVenders
        fields = '__all__'
        exclude = ('is_approved', 'user_type', 'user')
        widgets = {
            'franchise_description': forms.Textarea(attrs={'rows': 3}),
        }
    