from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=100)
    date_hired = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

