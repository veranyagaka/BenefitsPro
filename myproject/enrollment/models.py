from django.db import models
#from benefits.models import Benefits

# Create your models here.
class Employee(models.Model):
    EMPLOYEE_STATUS_CHOICES = [
        ('active', 'Active'),
        ('on leave', 'On Leave'),
        ('terminated', 'Terminated')
    ]
    
    EMPLOYEE_TYPE_CHOICES = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('temporary', 'Temporary')
    ]
    password = models.CharField(max_length=255, default='1234', null=True)
    employee_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email_address = models.EmailField(max_length=100, unique=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employee_status = models.CharField(
        max_length=10,
        choices=EMPLOYEE_STATUS_CHOICES,
        default='active'
    )
    employee_type = models.CharField(
        max_length=10,
        choices=EMPLOYEE_TYPE_CHOICES,
        default='full-time'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.employee_id}"
    class Meta:
        db_table = 'employee'
        
class EmployeeBenefits(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #benefit = models.ForeignKey(Benefits, on_delete=models.CASCADE)
    health_insurance = models.BooleanField(default=False)
    dental_insurance = models.BooleanField(default=False)
    vision_insurance = models.BooleanField(default=False)
    life_insurance = models.BooleanField(default=False)
    retirement_savings = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - Benefits"
    class Meta:
        app_label = 'enrollment'
        #db_table = 'employee_benefits'

