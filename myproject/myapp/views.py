from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from enrollment.models import Employee
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import EmployeeUpdateForm



def login_view(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')
        try:
            employee = Employee.objects.get(employee_id=employee_id, password=password)
            # If employee exists, set session variable and redirect to profile
            request.session['employee_id'] = employee.employee_id
            return redirect('profile')
        except Employee.DoesNotExist:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')
    
@login_required
def profile_view(request):
    # Assuming employee_id is stored in session
    employee_id = request.session.get('employee_id')
    print(f"Employee ID from session: {employee_id}")

    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            if request.method == 'POST':
                form = EmployeeUpdateForm(request.POST, instance=employee)
                if form.is_valid():
                    form.save()
                    return redirect('profile')  # Redirect to the profile page after saving
            else:
                form = EmployeeUpdateForm(instance=employee)

            context = {
                'form': form,
                'employee': employee,
            }
            print(f"Employee found: {employee.first_name} {employee.last_name}")
            return render(request, 'profile.html', context)
        except Employee.DoesNotExist:
            print("Employee not found in database")
            # Handle the case where the employee does not exist
            return redirect('enrollment')  # Redirect to the enrollment page or login page
    else:
        # Handle the case where employee_id is not in the session
        print("Employee ID not found in session")
        return redirect('enrollment')  # Redirect to the enrollment page or login page
    
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
