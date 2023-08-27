from django.contrib import admin
from .models import Domain


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    model = Domain
    list_display = ("id", "domain_name", "ping_of_domain")
    readonly_fields = ('ping_of_domain',)
