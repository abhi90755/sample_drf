from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import *

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_student(request):
    student = Student.objects.all()
    serializer = StudentSerializers(student, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
     serializer.save()
     return Response( {'message' : 'sent','data': serializer.data})
    return Response(serializer.errors)


@api_view(['PATCH'])
def post_student(request):
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
     serializer.save()
     return Response( {'message' : 'sent','data': serializer.data})
    return Response(serializer.errors)
