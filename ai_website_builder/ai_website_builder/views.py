from django.shortcuts import render

def login_view(request):
    return render(request, 'users/login.html', {})

def generate_view(request):
    return render(request, 'websites/generate.html', {})

def manage_view(request):
    return render(request, 'websites/manage.html', {})
