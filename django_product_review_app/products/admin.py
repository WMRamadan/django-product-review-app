from django.contrib import admin

from .models import Review, Product, Category

admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Category)
