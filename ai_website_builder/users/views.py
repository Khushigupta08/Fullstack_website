from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        response = requests.post(
            'http://localhost:8000/users/api/register/',
            json={
                'email': request.POST.get('email'),
                'password': request.POST.get('password')
            },
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            messages.success(request, 'Registration successful! Please login.')
            return redirect('users:login')
        else:
            try:
                error_message = response.json().get('error', 'Registration failed')
                messages.error(request, error_message)
            except:
                messages.error(request, 'Something went wrong!')
    return render(request, 'users/register.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        response = requests.post(
            'http://localhost:8000/users/api/login/',
            json={
                'email': email,
                'password': password
            },
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access')
            if access_token:
                request.session['access_token'] = access_token
                return redirect('websites:generate')  
            else:
                messages.error(request, "Login failed.")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'users/login.html')


# users/views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def refresh_token(request):
    refresh_token = request.data.get('refresh_token')

    try:
        # Create a RefreshToken object from the provided refresh token
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token}, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=400)
