from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from appone.serializer import *
from appone.models import *

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class StudentOps(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset =Student.objects.all()
    serializer_class = StudentSerializer

class UserProfiOps(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset =UserProfi.objects.all()
    serializer_class = UserProfiSerializer






