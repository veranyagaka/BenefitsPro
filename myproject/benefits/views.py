from django.shortcuts import render
from enrollment.models import Employee
from benefits.models import Application


# Create your views here.
def benefits_view(request):
    
    #return render(request, 'benefits.html')
    employee_id = request.session.get('employee_id')
    employee = Employee.objects.get(employee_id=employee_id)

    applications = Application.objects.filter(employee=employee)

    accepted_benefits = Application.objects.filter(status='Accepted')
    pending_benefits = Application.objects.filter(status='Pending')
    rejected_benefits = Application.objects.filter(status='Rejected')
    context = {
                'employee': employee,
                'accepted_benefits': accepted_benefits,
                'pending_benefits': pending_benefits,
                'rejected_benefits': rejected_benefits,
                'applications': applications,

            }
    return render(request, 'benefits.html', context)