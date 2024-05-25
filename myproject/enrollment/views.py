from django.shortcuts import render, redirect
from .models import EmployeeBenefits, Employee
from benefits.models import Benefits

def enrollment(request):
    #return render(request, 'enrollment.html')
    benefits = Benefits.objects.all()
    return render(request, 'enrollment.html', {'benefits': benefits})

def process_enrollment(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        selected_benefits = request.POST.getlist('benefits[]')

        
        # Check if employee exists in Employee table
        if Employee.objects.filter(employee_id=employee_id, last_name=last_name, first_name=first_name).exists():
            employee = Employee.objects.get(employee_id=employee_id, last_name=last_name, first_name=first_name)
            
            # Remove previous benefits
            employee.employee_benefits.all().delete()
            
            # Add selected benefits to the employee
            for benefit_id in selected_benefits:
                benefit = Benefits.objects.get(id=benefit_id)
                EmployeeBenefits.objects.create(employee=employee, benefit=benefit)
            
            return redirect('profile')  # Redirect to profile page (make sure to define this URL)
        else:
            return render(request, 'enrollment_fail.html', {'message': 'Employee not found'})

    return redirect('enrollment')
