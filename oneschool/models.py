from django.db import models

# Create your models here.

class CourseDetails(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)


    
