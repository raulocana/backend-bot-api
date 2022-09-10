from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _

from api.tickets.models import Ticket


class TicketAdmin(ModelAdmin):

    list_display = (
        "uuid",
        "topic",
    )
    search_fields = (
        "uuid",
        "user__uuid",
        "topic",
        "question",
    )

    ordering = ("date_created",)

    fieldsets = (
        (_("User Info"), {"fields": ("user",)}),
        (_("Question info"), {"fields": ("topic", "question")}),
        (_("Important dates"), {"fields": ("date_created",)}),
    )


admin.site.register(Ticket, TicketAdmin)
