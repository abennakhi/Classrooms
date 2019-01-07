from django.db import models
from django.contrib.auth.models import User
from django import forms

genders = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('Apache Helicopter', 'Others'),
)


class Classroom(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    year = models.IntegerField()
    teacher = models.ForeignKey(
        User,  on_delete=models.CASCADE, related_name="teacher_id")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=genders)
    exam_grade = models.IntegerField()
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="class_id")
    image = models.ImageField()

    def __str__(self):
        return self.name
