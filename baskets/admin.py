from django.contrib import admin

from baskets.models import Baskets


class BasketAdmin(admin.TabularInline):
    model = Baskets
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
