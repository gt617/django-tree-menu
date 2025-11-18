from django.contrib import admin
from .models import Menu, MenuItem


class InlineModel(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [InlineModel]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "menu", "parent"]
    search_fields = ["name"]
