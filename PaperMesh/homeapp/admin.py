from django.contrib import admin
from .models import Category, Fashion 


class FashionAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'item_name', 'price', 'item_img')
    list_filter = ('category',)  # Add filters if needed
    search_fields = ('item_name', 'category__category_name')  # Add search fields if needed
    readonly_fields = ('product_id',)  # Make UUID field read-only

admin.site.register(Category)
admin.site.register(Fashion, FashionAdmin)  