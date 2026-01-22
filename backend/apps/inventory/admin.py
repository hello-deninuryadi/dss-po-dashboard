from django.contrib import admin
from .models import Item

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_code',
        'item_name',
        'current_stock',
        'avg_monthly_sales',
        'lead_time_days',
        'is_active',
    )
    
    search_fields = ('item_code', 'item_name')
    list_filter = ('is_active',)

