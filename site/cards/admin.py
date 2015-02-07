from django.contrib import admin

from .models import Card, CardContent, CardTag


class CardContentInline(admin.StackedInline):
    model = CardContent


class CardTagInline(admin.StackedInline):
    model = CardTag
    extra = 3


class CardAdmin(admin.ModelAdmin):
    inlines = [CardContentInline, CardTagInline]

    def save_formset(self, request, form, formset, change):
        formset.save()
        if change:
            return
        for f in formset.forms:
            if isinstance(f.instance, CardContent):
                f.instance.author = request.user
                f.instance.save()


admin.site.register(Card, CardAdmin)
