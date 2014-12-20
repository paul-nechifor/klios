from django.contrib import admin
from .models import Card, CardContent, CardAnswer, CardTag


class CardContentInline(admin.StackedInline):
    model = CardContent


class CardTagInline(admin.StackedInline):
    model = CardTag
    extra = 3


class CardAdmin(admin.ModelAdmin):
    inlines = [CardContentInline, CardTagInline]


admin.site.register(Card, CardAdmin)
