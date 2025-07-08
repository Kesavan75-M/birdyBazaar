from django.contrib import admin
from .models import BirdProduct, Customer, Vendor

# Custom admin view for BirdProduct
class BirdProductAdmin(admin.ModelAdmin):
    list_display = ('bird_type', 'price', 'vendor', 'weight', 'age')
    search_fields = ('bird_type', 'niram', 'vendor__username')  # optional search
    list_filter = ('bird_type', 'vendor')  # optional filter

# Registering models
admin.site.register(BirdProduct, BirdProductAdmin)
admin.site.register(Customer)
admin.site.register(Vendor)
