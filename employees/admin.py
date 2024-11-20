from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'date_hired')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    list_filter = ('position', 'date_hired')

