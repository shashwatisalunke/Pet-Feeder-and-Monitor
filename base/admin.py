from django.contrib import admin
from .models import MyUser, Pet

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Pet)