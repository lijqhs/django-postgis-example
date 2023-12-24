from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        # 'cuisine_type',
        'address',
        'lon', 'lat',
    )

    fieldsets = [
        ('Basic Information', {
            'fields': (
                'brand',
            )
        }),
        ('Cuisine Information', {
            'fields': (
                'cuisine_type',
            )
        }),
        ('Location Information', {
            'fields': (
                'address',
            )
        }),
        ('Geo Information', {
            'fields': (
                ('lon', 'lat'),
            )
        }),        
    ]