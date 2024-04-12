
from enum import unique
from pyexpat import model
from django.db import models


# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=15,unique=True)
    course_desc = models.CharField(max_length=150)
    file = models.FileField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_title

class StudentDetail(models.Model):
    std_name = models.CharField(max_length=100)
    std_email = models.CharField(max_length=100)
    std_number = models.CharField(max_length=100)
    std_qualification = models.CharField(max_length=100)
    std_course = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.std_name

class CourseDownload(models.Model):
    std_name = models.CharField(max_length=100)
    std_email = models.CharField(max_length=100)
    std_number = models.CharField(max_length=100)
    std_qualification = models.CharField(max_length=100)
    std_download_course = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.std_download_course


class CertificateDetail(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    cert_number = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Course_name = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.cert_number