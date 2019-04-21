from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from School.serializers import StudentSerializer
from .models import Student 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def StudentInfo(request):
	if request.method=='GET':
	    snippets = Student.objects.all()
	    serializer = StudentSerializer(snippets,many=True)
	    return Response(serializer.data)


