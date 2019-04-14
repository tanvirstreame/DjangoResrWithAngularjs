from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student 

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Student
		fields=('url','name','sid','age','studyLevel')
