from django.contrib import admin
from .models import Product, Category, CategoryProduct

admin.site.register([Product, Category, CategoryProduct])
