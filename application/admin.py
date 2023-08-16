from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from application.models import Employee, Order


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "probation")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position", "probation")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info",
         {"fields": ("first_name", "last_name", "position", "probation")}),
    )


admin.site.register(Order)
