# yourapp/middleware.py
from django.shortcuts import redirect

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if not request.session.get('employee_id') and path not in ['','/login/', '/register/']:
            return redirect('login_view')
        response = self.get_response(request)
        return response
