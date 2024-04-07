from django.contrib import admin

from advertisements.models import Advertisement


# Register your models here.
class AdvertisementInline(admin.TabularInline):
    model = Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [AdvertisementInline]
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']
