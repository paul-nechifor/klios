from django.contrib import admin
from .models import Card, CardContent, CardAnswer


class CardContentInline(admin.StackedInline):
    model = CardContent


class CardAdmin(admin.ModelAdmin):
    inlines = [CardContentInline]


admin.site.register(Card, CardAdmin)
