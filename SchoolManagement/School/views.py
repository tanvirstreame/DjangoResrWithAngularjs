from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from School.serializers import StudentSerializer
from .models import Student 

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer