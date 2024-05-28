from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, redirect
from enrollment.models import Employee
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import EmployeeUpdateForm
#from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from benefits.models import Application

def login_view(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')
        try:
            employee = Employee.objects.get(employee_id=employee_id, password=password)
            # If user exists, set session variable and redirect to profile
            request.session['employee_id'] = employee.employee_id
            return redirect('profile')
        except Employee.DoesNotExist:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid Employee ID or password'})
    elif request.method == 'GET':
        # This block will be executed when the form is loaded
        # and a GET request is made to the login page
        print('smths not right')
        return render(request, 'login.html')
    else:
        # This block will be executed for any other request method
        # It's a good idea to log these cases for debugging purposes
        print(f'Unexpected request method: {request.method}')
        return HttpResponseBadRequest('Bad request method')
    
#@login_required
def profile_view(request):
    # Assuming employee_id is stored in session
    employee_id = request.session.get('employee_id')
    print(f"Employee ID from session: {employee_id}")

    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            applications = Application.objects.filter(employee=employee)

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
                'applications': applications,
            }
            print(f"Employee found: {employee.first_name} {employee.last_name}")
            return render(request, 'profile.html', context)
        except Employee.DoesNotExist:
            print("Employee not found in database")
            # Handle the case where the employee does not exist
            return redirect('register')  # Redirect to the enrollment page or login page
    else:
        # Handle the case where employee_id is not in the session
        return redirect('login')   # Redirect to the enrollment page or login page

#to handle form submission
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            return render(request, 'success.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import logout as auth_logout
#from django.urls import reverse


def logout_view(request):
    print("Logging out...")
    auth_logout(request)
    print("Redirecting to login...")
    return redirect('login_view')

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def settings_view(request):
    employee_id = request.session.get('employee_id')

    employee = Employee.objects.get(employee_id=employee_id)
    context = {
                'employee': employee,
            }
    return render(request, 'user_settings.html', context)

