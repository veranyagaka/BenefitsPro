from django.db import models
from enrollment.models import Employee

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    #class Meta:
        #db_table = 'users'

class Dependent(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - Dependent of {self.employee.first_name} {self.employee.last_name}"
    class Meta:
        db_table = 'dependent'

class Beneficiary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - Beneficiary of {self.employee.first_name} {self.employee.last_name}"
    class Meta:
        db_table = 'beneficiary'
