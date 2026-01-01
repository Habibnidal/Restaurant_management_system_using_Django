# FoodHub - Professional Food Ordering System

A comprehensive Django-based food ordering platform that connects customers with restaurants, featuring a modern UI, shopping cart functionality, and franchise management system.

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Installation & Setup](#installation--setup)
5. [Project Structure](#project-structure)
6. [Database Models](#database-models)
7. [URL Routing](#url-routing)
8. [Views & Functionality](#views--functionality)
9. [Templates](#templates)
10. [Static Files & Styling](#static-files--styling)
11. [User Roles & Permissions](#user-roles--permissions)
12. [Configuration](#configuration)
13. [Usage Guide](#usage-guide)
14. [Deployment](#deployment)

---

## 🎯 Project Overview

FoodHub is a full-featured food ordering system built with Django that allows:
- **Customers** to browse restaurants, view menus, add items to cart, and place orders
- **Vendors** to register restaurants, manage menus, and handle franchise opportunities
- **Admins** to approve vendors and manage the platform

The system features a modern, responsive design with a professional teal/cyan color scheme, built entirely with Django, HTML, CSS, and Bootstrap (no custom JavaScript).

---

## ✨ Features

### Customer Features
- User registration and authentication
- Browse approved restaurants
- View restaurant details and menus
- Add food items to shopping cart
- Update cart quantities
- View order summary with tax and delivery fees
- Secure payment page with QR code
- Customer dashboard with profile management

### Vendor Features
- Vendor registration with restaurant details
- Restaurant profile management
- Add, edit, and delete food items
- Upload food images
- View accepted franchise requests
- Franchise opportunity management
- Vendor dashboard

### Admin Features
- Approve/reject vendor registrations
- Manage all users and restaurants
- View franchise requests
- Full Django admin panel access

### Additional Features
- Franchise request system
- Shopping cart with quantity management
- Tax calculation (5% GST)
- Delivery fee calculation
- Image uploads for users, restaurants, and food items
- reCAPTCHA integration for registration
- Responsive design for all devices
- Professional UI with modern styling

---

## 🛠 Technology Stack

### Backend
- **Django 5.2.7** - Web framework
- **Python 3.x** - Programming language
- **SQLite** - Database (development)

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with custom CSS variables
- **Bootstrap 5.3.8** - UI framework
- **Font Awesome 6.4.0** - Icons

### Django Packages
- **django-crispy-forms** - Form styling
- **crispy-bootstrap5** - Bootstrap 5 integration
- **django-recaptcha** - reCAPTCHA integration

### Design
- **Custom CSS** - Professional styling system
- **CSS Variables** - Consistent theming
- **Responsive Grid** - Mobile-first design
- **Gradient Effects** - Modern visual appeal

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Navigate to Project
```bash
cd MODULE_3/module3
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django==5.2.7
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install django-recaptcha
```

Or create a `requirements.txt`:
```txt
Django==5.2.7
django-crispy-forms==2.1
crispy-bootstrap5==2024.2
django-recaptcha==5.0.0
Pillow==10.0.0
```

Then install:
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```
MODULE_3/module3/
│
├── accounts/                 # Customer account management
│   ├── models.py            # UserDetails model
│   ├── views.py             # Authentication & customer views
│   ├── forms.py             # User registration forms
│   ├── urls.py              # Account URL patterns
│   └── context_processors.py # User type context processor
│
├── venders/                  # Vendor/Restaurant management
│   ├── models.py            # multiVenders, foodItem, FranchiseRequest
│   ├── views.py             # Vendor views & food management
│   ├── forms.py             # Vendor registration forms
│   └── urls.py              # Vendor URL patterns
│
├── cart/                     # Shopping cart functionality
│   ├── models.py            # Cart, CartItem models
│   ├── views.py             # Cart operations
│   ├── urls.py              # Cart URL patterns
│   └── templates/cart/      # Cart templates
│
├── module3/                  # Project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Root URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   ├── login.html           # Login page
│   ├── registration.html    # Registration page
│   ├── dashboard.html       # General dashboard
│   ├── accounts/            # Customer templates
│   ├── cart/               # Cart templates
│   └── venders/            # Vendor templates
│
├── static/                   # Static files
│   ├── css/
│   │   └── main.css         # Main stylesheet
│   └── images/              # Static images
│
├── media/                    # User-uploaded files
│   ├── userimg/            # User profile images
│   ├── restaurent_pics/    # Restaurant images
│   ├── foodimg/            # Food item images
│   └── licience_pics/      # License documents
│
├── manage.py                 # Django management script
└── db.sqlite3               # SQLite database
```

---

## 🗄 Database Models

### Accounts App

#### `userDetails`
Stores additional customer information.

```python
- user: OneToOneField(User) - Links to Django User
- phone: BigIntegerField - Contact number
- house_no: PositiveIntegerField - House number
- street: CharField(100) - Street address
- city: CharField(100) - City
- state: CharField(100) - State
- zipcode: CharField(100) - ZIP code
- img: ImageField - Profile picture
- user_type: CharField(100) - Default: 'customer'
```

### Venders App

#### `multiVenders`
Restaurant/Vendor information.

```python
- user: OneToOneField(User) - Vendor user account
- restaurent_name: CharField(100) - Restaurant name
- address: CharField(100) - Address
- city: CharField(100) - City
- state: CharField(100) - State
- zipcode: CharField(100) - ZIP code
- restaurent_lic: ImageField - License document
- restaurent_img: ImageField - Restaurant image
- is_approved: BooleanField - Admin approval status
- user_type: CharField(100) - Default: 'vender'
- is_franchise_available: BooleanField - Franchise option
- franchise_investment: DecimalField - Investment amount
- agreement_years: PositiveIntegerField - Agreement duration
- profit_share_percentage: DecimalField - Profit share %
- franchise_description: TextField - Franchise details
```

#### `foodItem`
Food items in restaurant menus.

```python
- vender: ForeignKey(multiVenders) - Restaurant owner
- food_name: CharField(50) - Item name
- food_desc: CharField(100) - Description
- price: DecimalField(8,2) - Price
- food_img: ImageField - Food image
```

#### `FranchiseRequest`
Franchise requests from users.

```python
- vendor: ForeignKey(multiVenders) - Restaurant
- user: ForeignKey(User) - Requesting user
- status: CharField - 'pending', 'accepted', 'rejected'
- requested_at: DateTimeField - Request timestamp
- accepted_at: DateTimeField - Acceptance timestamp
```

### Cart App

#### `Cart`
User shopping cart.

```python
- user: OneToOneField(User) - Cart owner
- created_at: DateTimeField - Creation time
- updated_at: DateTimeField - Last update
```

#### `CartItem`
Items in the cart.

```python
- cart: ForeignKey(Cart) - Parent cart
- food_item: ForeignKey(foodItem) - Food item
- quantity: PositiveIntegerField - Quantity
- added_at: DateTimeField - Added timestamp

Properties:
- total_price: Calculated as quantity * food_item.price
```

---

## 🔗 URL Routing

### Root URLs (`module3/urls.py`)
```python
'' → accounts.urls
'vender/' → venders.urls (namespace: 'venders')
'cart/' → cart.urls
'admin/' → Django admin
```

### Accounts URLs (`accounts/urls.py`)
```python
'' → home (name: 'home')
'register/' → registration (name: 'register')
'login/' → user_login (name: 'login')
'logout/' → user_logout (name: 'logout')
'dashboard/vendor/' → vendor_dashboard (name: 'vendor_dashboard')
'dashboard/customer/' → customer_dashboard (name: 'customer_dashboard')
'update/' → update (name: 'update')
'forgot_password/' → forgot_password (name: 'forgot_password')
```

### Vendor URLs (`venders/urls.py`)
```python
'venderregister/' → venderRegister (name: 'venderregister')
'<int:id>/' → vender_details (name: 'venderdetails')
'addfood/' → addFood (name: 'addfood')
'foodedit/<int:id>/' → food_edit (name: 'foodedit')
'food/delete/<int:id>/' → food_delete (name: 'food_delete')
'edit/<int:id>/' → edit_vendor (name: 'edit_vendor')
'franchise/request/<int:vendor_id>/' → request_franchise (name: 'request_franchise')
'franchise/<int:vendor_id>/details/' → franchise_details (name: 'franchise_details')
'franchise/accepted/' → accepted_franchises (name: 'accepted_franchises')
```

### Cart URLs (`cart/urls.py`)
```python
'' → view_cart (name: 'view_cart')
'add/<int:food_item_id>/' → add_to_cart (name: 'add_to_cart')
'remove/<int:item_id>/' → remove_from_cart (name: 'remove_from_cart')
'update/<int:item_id>/' → update_cart_item (name: 'update_cart_item')
'increment/<int:item_id>/' → increment_cart_item (name: 'increment_cart_item')
'decrement/<int:item_id>/' → decrement_cart_item (name: 'decrement_cart_item')
'checkout/' → checkout (name: 'checkout')
```

---

## 👁 Views & Functionality

### Accounts Views

#### `registration(request)`
- Handles user registration
- Creates User and userDetails
- Uses reCAPTCHA validation
- Redirects to login on success

#### `user_login(request)`
- Authenticates users
- Determines user type (Customer/Vendor/Admin)
- Sets session variable
- Redirects to appropriate dashboard

#### `home(request)`
- Displays all approved restaurants
- Shows restaurant cards with images
- Requires login

#### `customer_dashboard(request)`
- Shows customer profile
- Displays user information
- Quick action links

#### `vendor_dashboard(request)`
- Shows vendor restaurant info
- Displays menu items
- Shows accepted franchises

#### `update(request)`
- Updates user profile
- Updates userDetails
- Redirects based on user type

#### `forgot_password(request)`
- Allows password reset
- Requires username and new password

### Vendor Views

#### `venderRegister(request)`
- Vendor registration
- Creates User and multiVenders
- Requires admin approval

#### `vender_details(request, id)`
- Shows restaurant details
- Displays menu items
- Shows franchise information
- Allows adding items to cart

#### `addFood(request)`
- Adds new food item to menu
- Handles image upload

#### `food_edit(request, id)`
- Edits existing food item
- Updates price, description, image

#### `food_delete(request, id)`
- Deletes food item from menu

#### `edit_vendor(request, id)`
- Edits restaurant profile
- Updates restaurant information

#### `franchise_details(request, vendor_id)`
- Shows franchise opportunity details
- Displays investment, agreement, profit share

#### `request_franchise(request, vendor_id)`
- Creates franchise request
- Sets status to 'pending'

#### `accepted_franchises(request)`
- Lists accepted franchise requests

### Cart Views

#### `view_cart(request)`
- Displays cart items
- Calculates subtotal, tax (5%), delivery fee (₹50)
- Shows total amount

#### `add_to_cart(request, food_item_id)`
- Adds food item to cart
- Creates cart if doesn't exist
- Increments quantity if item exists

#### `remove_from_cart(request, item_id)`
- Removes item from cart

#### `update_cart_item(request, item_id)`
- Updates item quantity
- Deletes if quantity < 1

#### `increment_cart_item(request, item_id)`
- Increases quantity by 1

#### `decrement_cart_item(request, item_id)`
- Decreases quantity by 1
- Prevents going below 1

#### `checkout(request)`
- Shows payment page
- Displays order summary
- Calculates final total with tax and delivery

---

## 🎨 Templates

### Base Template (`base.html`)
- Main layout template
- Navigation bar with user menu
- Footer with links
- Message alerts
- Bootstrap integration

### Key Templates

#### Authentication
- `login.html` - User login form
- `registration.html` - User registration with reCAPTCHA
- `forgot_password.html` - Password reset

#### Main Pages
- `index.html` - Home page with restaurant listings
- `dashboard.html` - General dashboard (role-based)
- `accounts/customer_dashboard.html` - Customer dashboard
- `venders/vendor_dashboard.html` - Vendor dashboard

#### Restaurant Pages
- `venders/vender_details.html` - Restaurant details and menu
- `venders/vender_register.html` - Vendor registration
- `venders/addfood.html` - Add food item
- `venders/foodedit.html` - Edit food item
- `venders/edit_vendor.html` - Edit restaurant profile
- `venders/franchise_details.html` - Franchise information

#### Cart Pages
- `cart/cart.html` - Shopping cart
- `cart/payment.html` - Payment/checkout page

#### Profile
- `update.html` - Update user profile

### Template Features
- Responsive design
- Professional styling
- Role-based content
- Form validation (HTML5)
- Image uploads
- Message displays

---

## 🎨 Static Files & Styling

### CSS Architecture

#### Main Stylesheet (`static/css/main.css`)
- **CSS Variables** - Centralized color scheme
- **Color Scheme**: Teal/Cyan theme
  - Primary: `#00B4D8`
  - Primary Dark: `#0077B6`
  - Primary Light: `#48CAE4`
- **Responsive Design** - Mobile-first approach
- **Animations** - Smooth transitions
- **Component Styles** - Cards, buttons, forms

#### Key CSS Features
- Gradient backgrounds
- Box shadows
- Hover effects
- Responsive grids
- Custom scrollbar
- Professional typography

### Static Images
- Logo/cover images
- QR code for payments
- Default profile images
- Placeholder images

### Media Files
- User profile images (`media/userimg/`)
- Restaurant images (`media/restaurent_pics/`)
- Food item images (`media/foodimg/`)
- License documents (`media/licience_pics/`)

---

## 👥 User Roles & Permissions

### Customer
- Register and login
- Browse restaurants
- View menus
- Add items to cart
- Place orders
- Update profile
- View customer dashboard

### Vendor
- Register restaurant
- Wait for admin approval
- Manage restaurant profile
- Add/edit/delete food items
- View franchise requests
- Manage franchise opportunities
- View vendor dashboard

### Admin
- Access Django admin panel
- Approve/reject vendors
- Manage all users
- View all restaurants
- Manage franchise requests
- Full system access

### User Type Detection
- Uses context processor (`accounts.context_processors.user_type`)
- Checks for `multivenders` relationship → Vendor
- Checks for `userdetails` relationship → Customer
- Otherwise → Admin

---

## ⚙️ Configuration

### Settings (`module3/settings.py`)

#### Installed Apps
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_recaptcha',
    'venders',
    'cart',
]
```

#### Middleware
- Security middleware
- Session middleware
- CSRF protection
- Authentication middleware
- Messages middleware

#### Database
- SQLite (development)
- Can be changed to PostgreSQL/MySQL for production

#### Static & Media Files
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
```

#### Crispy Forms
```python
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

#### reCAPTCHA
```python
RECAPTCHA_PUBLIC_KEY = 'your-public-key'
RECAPTCHA_PRIVATE_KEY = 'your-private-key'
```

#### Context Processors
- Request context
- Authentication context
- Messages context
- Custom user_type processor

---

## 📖 Usage Guide

### For Customers

1. **Registration**
   - Visit `/register/`
   - Fill in username, email, password
   - Add address details
   - Upload profile picture (optional)
   - Complete reCAPTCHA
   - Submit form

2. **Login**
   - Visit `/login/`
   - Enter credentials
   - Redirected to customer dashboard

3. **Browse Restaurants**
   - View home page
   - Click on restaurant card
   - View menu items

4. **Add to Cart**
   - Click "Add to Cart" on food item
   - Item added to cart
   - Cart count updates in navbar

5. **Manage Cart**
   - Visit cart page
   - Use +/- buttons to adjust quantity
   - Click "Remove" to delete items
   - View order summary

6. **Checkout**
   - Click "Proceed to Checkout"
   - Review order summary
   - View payment QR code
   - Complete payment

### For Vendors

1. **Registration**
   - Visit `/vender/venderregister/`
   - Create user account
   - Add restaurant details
   - Upload restaurant image
   - Upload license document
   - Submit for approval

2. **Wait for Approval**
   - Admin must approve registration
   - Restaurant appears after approval

3. **Add Food Items**
   - Login to vendor dashboard
   - Click "Add Food Item"
   - Enter name, description, price
   - Upload food image
   - Save item

4. **Manage Menu**
   - View all items in dashboard
   - Edit items
   - Delete items
   - Update restaurant profile

5. **Franchise Management**
   - Set franchise availability
   - Add investment details
   - Set agreement terms
   - View franchise requests

### For Admins

1. **Access Admin Panel**
   - Visit `/admin/`
   - Login with superuser credentials

2. **Approve Vendors**
   - Go to Venders → multiVenders
   - Select vendor
   - Check "is_approved"
   - Save

3. **Manage System**
   - View all users
   - Manage restaurants
   - Handle franchise requests
   - Monitor system activity

---

## 🚀 Deployment

### Production Checklist

1. **Security Settings**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECRET_KEY = 'your-secret-key'  # Use environment variable
   ```

2. **Database**
   - Switch from SQLite to PostgreSQL/MySQL
   - Update DATABASES in settings.py

3. **Static Files**
   - Run `python manage.py collectstatic`
   - Configure web server to serve static files
   - Use CDN or cloud storage for media files

4. **Environment Variables**
   - Store SECRET_KEY in environment
   - Store database credentials securely
   - Store reCAPTCHA keys

5. **HTTPS**
   - Enable SSL/TLS
   - Update CSRF settings
   - Secure cookie settings

6. **Web Server**
   - Use Gunicorn or uWSGI
   - Configure Nginx or Apache
   - Set up process manager (systemd/supervisor)

### Example Deployment Commands

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run with Gunicorn
gunicorn module3.wsgi:application --bind 0.0.0.0:8000
```

---

## 🔧 Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL and STATICFILES_DIRS
   - Verify web server configuration

2. **Media files not displaying**
   - Check MEDIA_URL and MEDIA_ROOT
   - Verify file permissions
   - Check URL configuration

3. **Forms not submitting**
   - Check CSRF token
   - Verify form method (POST)
   - Check form action URL

4. **User type not detected**
   - Verify context processor in settings
   - Check user has userdetails or multivenders
   - Clear browser cache

5. **Cart not working**
   - Verify user is logged in
   - Check Cart model relationships
   - Verify cart URLs

---

## 📝 Notes

- **No JavaScript**: Project uses only Django, HTML, CSS, and Bootstrap
- **Responsive Design**: Works on all device sizes
- **Image Uploads**: Requires Pillow library
- **reCAPTCHA**: Requires valid keys for production
- **Admin Approval**: Vendors need admin approval before appearing

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Admin
```bash
python manage.py createsuperuser
# Then visit /admin/
```

---

## 📞 Support

For issues or questions:
1. Check this documentation
2. Review Django documentation
3. Check template syntax
4. Verify URL patterns
5. Check model relationships

---

**Last Updated**: 2024
**Django Version**: 5.2.7
**Python Version**: 3.8+

