from django.contrib import admin
from shop.models import Item, Catagories


class ChoiceInline2(admin.StackedInline):
    model = Catagories
    extra = 3


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,               {'fields': ['desc']}),
	(None,               {'fields': ['price']}),
        (None,               {'fields': ['name']}),
    ]
    inlines = [ChoiceInline2]

admin.site.register(Item, ItemAdmin)
