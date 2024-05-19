from django import forms
from enrollment.models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'date_of_birth', 'email_address', 'department', 'position', 
            'hire_date', 'salary', 'employee_status', 'employee_type'
        ]