from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from enrollment.models import Employee
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            # If user exists, set session variable and redirect to profile
            request.session['username'] = user.username
            return redirect('profile')
        except User.DoesNotExist:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def profile_view(request):
    # Assuming employee_id is stored in session
    employee_id = request.session.get('employee_id')
    print(f"Employee ID from session: {employee_id}")
    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            context = {
                'first_name': employee.first_name,
                'last_name': employee.last_name,
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


def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
