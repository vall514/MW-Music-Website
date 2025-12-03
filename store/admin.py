from django.contrib import admin
from .models import Product, Donation

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'featured']
    list_filter = ['category', 'available', 'featured']
    search_fields = ['name', 'description']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'donor_email', 'amount', 'created_at']
    list_filter = ['created_at']
    search_fields = ['donor_name', 'donor_email']
    readonly_fields = ['created_at']