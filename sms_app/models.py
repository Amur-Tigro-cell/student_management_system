from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    department = models.CharField(max_length=100, default="")
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class personal_info(models.Model):
    student = models.OneToOneField(student, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.name}'s Personal Info"
