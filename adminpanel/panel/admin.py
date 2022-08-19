from django.contrib import admin

from .models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "user_id",
        "domen"
    )
