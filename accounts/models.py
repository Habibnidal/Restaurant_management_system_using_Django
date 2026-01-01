from django.db import models
from django.conf import settings


# Create your models here.

class userDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Additional fields
    
    phone = models.BigIntegerField()
    house_no = models.PositiveIntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    img = models.ImageField(upload_to='userimg/',blank=True, null=True)
    user_type = models.CharField(max_length=100, default='customer')

    def __str__(self):
        return str(self.user.username)

    