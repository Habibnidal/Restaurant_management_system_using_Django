from django.contrib import admin
from .models import multiVenders, foodItem, FranchiseRequest

admin.site.register(multiVenders)
admin.site.register(foodItem)
admin.site.register(FranchiseRequest)
