from typing import List
from django.contrib import admin
from .models import user

# Register your models here.
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
 List_display=['id','name','email','password']