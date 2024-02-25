from django.contrib import admin
from .models import Item


class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "parent"]


admin.site.register(Item, MenuAdmin)
