from django.db import models

# Create your models here.
class Benefits(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
