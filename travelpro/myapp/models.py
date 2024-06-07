from django.db import models

# Create your models here.

class contactdb(models.Model):
    name=models.CharField(max_length=150)
    mobile=models.CharField(max_length=150)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=250)
    def __str__(self):
        return self.name

