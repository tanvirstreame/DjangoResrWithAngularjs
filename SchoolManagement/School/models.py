from django.db import models


# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=80)
	sid=models.IntegerField()
	age=models.IntegerField()
	studyLevel=models.CharField(max_length=80)
		
	def __str__(self):
		return self.name