from django.db import models

# Create your models here.

class Courses(models.Model):
    course = models.CharField(max_length=50)

class Subjects(models.Model):
    subject = models.CharField(max_length=50)
    COURSES = models.ForeignKey(Courses, on_delete = models.CASCADE)

class ContactBook(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    photo = models.CharField(max_length=50)
    SUBJECTS = models.ForeignKey(Subjects, on_delete = models.CASCADE)

