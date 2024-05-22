from django.shortcuts import render

# Create your views here.
def benefits_view(request):
    return render(request, 'benefits.html')