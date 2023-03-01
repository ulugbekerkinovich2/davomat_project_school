from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters

from basic_app import models, serializer


# Create your views here.

class ListUsers(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserSerializer1


class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserPasswordSerializer


class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
