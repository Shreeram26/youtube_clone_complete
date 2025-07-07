from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import status

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not username or not email or not password:
        return Response({'error': 'All fields are required'}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User created successfully'}, status=201)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({'message': 'Login successful'})
    return Response({'error': 'Invalid credentials'}, status=400)
