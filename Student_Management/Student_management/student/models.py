from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    department = models.CharField(max_length=100, choices=[('CS', 'Computer Science'), ('ME', 'Mechanical'), ('EE', 'Electrical')])
    status = models.BooleanField(default=True) 

    def __str__(self):
        return self.name
