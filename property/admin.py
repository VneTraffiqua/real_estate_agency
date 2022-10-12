from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address')
    readonly_fields = ['created_at']
    raw_id_fields = ('likes', )


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat_complaint')


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town'
    )
    list_editable = ['new_building']
    list_filter = ('rooms_number', 'has_balcony', 'new_building')


admin.site.register(Flat, ItemAdmin)
admin.site.register(Complaint, ComplaintAdmin)
