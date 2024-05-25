from django.db import models
from enrollment.models import Employee
# Create your models here.
class Benefits(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
# application model
class Application(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    #employee_id = models.CharField(max_length=255)
    #last_name = models.CharField(max_length=255)
    #first_name = models.CharField(max_length=255)
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied')
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_applied = models.DateField(auto_now_add=True)
    benefits = models.ManyToManyField(Benefits)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.date_applied}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.status = 'Pending'
        super().save(*args, **kwargs)