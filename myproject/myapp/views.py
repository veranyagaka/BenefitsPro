from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
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
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'profile.html', {'username': username})

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
