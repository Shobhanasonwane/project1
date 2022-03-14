from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField()
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    salary=models.IntegerField()

    def __str__(self):
        return self.name
