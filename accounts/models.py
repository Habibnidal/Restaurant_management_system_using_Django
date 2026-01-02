from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.

class userDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    phone = models.BigIntegerField(null=True, blank=True)
    house_no = models.PositiveIntegerField(null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)

    img = CloudinaryField('image', blank=True, null=True)
    user_type = models.CharField(max_length=100, default='customer')



    def __str__(self):
        return str(self.user.username)

    