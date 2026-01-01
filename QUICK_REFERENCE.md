# FoodHub - Quick Reference Guide

## 🚀 Quick Start

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install django==5.2.7 django-crispy-forms crispy-bootstrap5 django-recaptcha Pillow

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 📍 Important URLs

| URL | Description | Access |
|-----|-------------|--------|
| `/` | Home page | Authenticated |
| `/register/` | Customer registration | Public |
| `/login/` | Login page | Public |
| `/vender/venderregister/` | Vendor registration | Public |
| `/dashboard/customer/` | Customer dashboard | Customer |
| `/dashboard/vendor/` | Vendor dashboard | Vendor |
| `/vender/<id>/` | Restaurant details | Public |
| `/cart/` | Shopping cart | Customer |
| `/cart/checkout/` | Payment page | Customer |
| `/admin/` | Admin panel | Admin |

## 🔑 User Types

| Type | Model | Access Level |
|------|-------|--------------|
| Customer | `userdetails` | Browse, Order, Cart |
| Vendor | `multivenders` | Manage Restaurant, Menu |
| Admin | Django User | Full Access |

## 📊 Key Models

### UserDetails (Customer)
```python
user, phone, house_no, street, city, state, zipcode, img, user_type
```

### multiVenders (Vendor)
```python
user, restaurent_name, address, city, state, zipcode, 
restaurent_lic, restaurent_img, is_approved, user_type,
is_franchise_available, franchise_investment, agreement_years,
profit_share_percentage, franchise_description
```

### foodItem
```python
vender, food_name, food_desc, price, food_img
```

### Cart
```python
user, created_at, updated_at
```

### CartItem
```python
cart, food_item, quantity, added_at
# Property: total_price
```

## 🎨 Color Scheme

```css
--primary-color: #00B4D8    /* Teal */
--primary-dark: #0077B6     /* Dark Blue */
--primary-light: #48CAE4   /* Light Cyan */
```

## 🔐 Authentication Flow

1. User registers → Creates User + userDetails
2. User logs in → Authenticates → Determines role
3. Redirects based on role:
   - Customer → `/dashboard/customer/`
   - Vendor → `/dashboard/vendor/`
   - Admin → `/admin/`

## 🛒 Cart Flow

1. Customer adds item → `cart:add_to_cart`
2. Item added to Cart → Creates CartItem
3. View cart → `cart:view_cart`
4. Update quantity → `cart:increment_cart_item` / `cart:decrement_cart_item`
5. Checkout → `cart:checkout`
6. Payment → Shows QR code

## 💰 Pricing Calculation

```
Subtotal = Sum of (item.price * item.quantity)
Tax = Subtotal * 0.05 (5% GST)
Delivery Fee = ₹50.00
Total = Subtotal + Tax + Delivery Fee
```

## 📁 File Upload Locations

- User Images: `media/userimg/`
- Restaurant Images: `media/restaurent_pics/`
- Food Images: `media/foodimg/`
- License Documents: `media/licience_pics/`

## 🔧 Common Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Start shell
python manage.py shell
```

## 🎯 Key Features

✅ No JavaScript (Pure Django/HTML/CSS)  
✅ Responsive Design  
✅ Role-based Access  
✅ Shopping Cart  
✅ Image Uploads  
✅ Franchise System  
✅ Tax Calculation  
✅ Professional UI  

## 📝 Template Tags Used

```django
{% load static %}
{% load crispy_forms_tags %}
{% extends "base.html" %}
{% block start %}{% endblock %}
{% url 'name' %}
{% if user.is_authenticated %}
{% if user_type == 'customer' %}
```

## 🚨 Important Notes

- Vendors need admin approval (`is_approved=True`)
- Cart requires authentication
- Only customers can add to cart
- Tax is 5% GST
- Delivery fee is ₹50.00
- Images require Pillow library

## 🔗 URL Namespaces

- Accounts: No namespace
- Vendors: `venders:`
- Cart: `cart:`

## 📱 Responsive Breakpoints

- Mobile: < 576px
- Tablet: 576px - 768px
- Desktop: > 768px

## 🎨 CSS Classes

- `.dashboard-card` - Dashboard card styling
- `.food-card` - Food item card
- `.restaurant-card` - Restaurant card
- `.cart-item` - Cart item styling
- `.auth-card` - Authentication card
- `.hero-section` - Hero banner

## 🔄 Context Variables

- `user` - Current user
- `user_type` - User type (customer/vender/admin)
- `venders` - All approved restaurants
- `cart_items` - Cart items
- `total` - Cart total
- `subtotal` - Cart subtotal
- `tax` - Tax amount
- `delivery_fee` - Delivery fee

