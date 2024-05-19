from django.contrib import admin

# Register your models here.
from .models import EmployeeBenefits

admin.site.register(EmployeeBenefits)
from .models import Employee

admin.site.register(Employee)