from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class teacher(models.Model):
    teacher_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)
class student(models.Model):
    teachers=models.ManyToManyField(teacher)
    student_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)

    def taught_by(self):
        return ",".join([str(teacher.teacher_id) for teacher in self.teachers.all()])




