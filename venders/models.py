from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


# Create your models here.

class multiVenders(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    
    restaurent_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    # restaurent_lic = models.ImageField(upload_to='licience_pics', blank=True, null=True)
    # restaurent_img = models.ImageField(upload_to='restaurent_pics', blank=True, null=True)
    restaurent_img = CloudinaryField('restaurant_image',blank=True,null=True)
    restaurent_lic = CloudinaryField('restaurant_license',blank=True,null=True)

    is_approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=100, default='vender', editable=False)

    # Franchise fields
    is_franchise_available = models.BooleanField(default=False)
    franchise_investment = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    agreement_years = models.PositiveIntegerField(null=True, blank=True)
    profit_share_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    franchise_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class foodItem(models.Model):
    vender = models.ForeignKey(multiVenders, on_delete=models.CASCADE, related_name='food_items')
    food_name = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # food_img = models.ImageField(upload_to='foodimg', blank=True, null=True)
    food_img = CloudinaryField('food_image',blank=True,null=True)
    
    def __str__(self):
        return self.food_name
# In venders/models.py
class FranchiseRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    vendor = models.ForeignKey(multiVenders, on_delete=models.CASCADE, related_name='franchise_requests')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Franchise request for {self.vendor.restaurent_name} by {self.user.username}"


