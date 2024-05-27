from django.shortcuts import render
from enrollment.models import Employee

# Create your views here.
def benefits_view(request):
    
    #return render(request, 'benefits.html')
    employee_id = request.session.get('employee_id')

    employee = Employee.objects.get(employee_id=employee_id)
    context = {
                'employee': employee,
            }
    return render(request, 'benefits.html', context)