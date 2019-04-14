from django.db import models


# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=80)
	sid=models.IntegerField(max_length=80)
	age=models.IntegerField(max_length=80)
	studyLevel=models.CharField(max_length=80)
		