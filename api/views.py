from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User, Test, Result

from .serializers import UserSerializer

# Create your views here.
# create user registrations views
class UserRegistrationView(APIView):
    def post(self, request: Request):
        data1 = request.data
        print(data1)
        serializer = UserSerializer(data=data1 )
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# create longin user views
class UserLoginView(APIView):
    def post(self, request: Request):
        login = request.data.get('login')
        password = request.data.get('password')
        user = User.objects.filter(login=login, password=password)
        if user:
            data = {"user": "Welcom site"}
            return Response(data=data, status=status.HTTP_200_OK)
        return Response({'error': "login yoki parol xato yoki siz tizimda ro'yxatdan o'tmagansiz"}, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [IsAuthenticated]
    def get(self, request: Request):
        # this function work superadmin authenticated
        # get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
