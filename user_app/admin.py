from django.contrib import admin
from .models import UserModel, UserAddress

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserAddress)
