from django.contrib import admin
from .models import User, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    ordering = ['name']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'date']
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
