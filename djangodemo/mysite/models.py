from django.db import models
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField(default=18)

    def __str__(self):
        return (self.first_name + '---' + self.email)

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + '---' + self.email)


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + '---' + self.email)


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + '---' + self.email)