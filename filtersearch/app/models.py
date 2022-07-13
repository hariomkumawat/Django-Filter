from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

   title = models.CharField(max_length=250)
   description = models.CharField(max_length=250)
   assigned_to = models.ManyToManyField(User)
   creation_date = models.DateField(auto_now=True)
   due_date = models.DateField(blank=True, null=True)
   completed = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)