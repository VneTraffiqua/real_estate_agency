from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address')
    readonly_fields = ['created_at']


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town'
    )
    list_editable = ['new_building']
    list_filter = ('rooms_number', 'has_balcony', 'new_building')


admin.site.register(Flat, ItemAdmin)
