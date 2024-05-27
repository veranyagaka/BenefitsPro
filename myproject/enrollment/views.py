from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeBenefits, Employee
from benefits.models import Benefits, Application
from django.apps import apps


def enrollment(request):
    #return render(request, 'enrollment.html')
    employee_id = request.session.get('employee_id')

    employee = Employee.objects.get(employee_id=employee_id)
    benefits = Benefits.objects.all()
    context = {
                'employee': employee,
                'benefits': benefits,
            }
    return render(request, 'enrollment.html', context)
    #benefits = Benefits.objects.all()
    #return render(request, 'enrollment.html', {'benefits': benefits})


def process_enrollment(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        selected_benefits = request.POST.getlist('benefits[]')
        # Check if employee exists in Employee table
        if Employee.objects.filter(employee_id=employee_id, last_name=last_name, first_name=first_name).exists():
            employee = Employee.objects.get(employee_id=employee_id, last_name=last_name, first_name=first_name)
            application = Application(employee=employee)
            application.save()  # Save to get an ID for the many-to-many relationship

        # Add selected benefits to the application
            for benefit_id in selected_benefits:
                benefit = get_object_or_404(Benefits, id=benefit_id)
                application.benefits.add(benefit)
                application.save()
            return redirect('profile')  # Redirect to profile page (make sure to define this URL)
        else:
            return render(request, 'enrollment_fail.html', {'message': 'Employee not found'})

    return redirect('enrollment')
