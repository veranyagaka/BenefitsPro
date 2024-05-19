from django.shortcuts import render, redirect
from .models import EmployeeBenefits, Employee

def enrollment(request):
    return render(request, 'enrollment.html')

def process_enrollment(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        health_insurance = 'health_insurance' in request.POST
        dental_insurance = 'dental_insurance' in request.POST
        vision_insurance = 'vision_insurance' in request.POST
        life_insurance = 'life_insurance' in request.POST
        retirement_savings = 'retirement_savings' in request.POST

        # Check if employee exists in Employee table
        if Employee.objects.filter(employee_id=employee_id, last_name=last_name, first_name=first_name).exists():
            # Create or update employee benefits
            EmployeeBenefits.objects.update_or_create(
                employee_id=employee_id,
                defaults={
                    'last_name': last_name,
                    'first_name': first_name,
                    'health_insurance': health_insurance,
                    'dental_insurance': dental_insurance,
                    'vision_insurance': vision_insurance,
                    'life_insurance': life_insurance,
                    'retirement_savings': retirement_savings
                }
            )
            return redirect('profile')  # Redirect to profile page (make sure to define this URL)
        else:
            return render(request, 'enrollment_fail.html', {'message': 'Employee not found'})

    return redirect('enrollment')
