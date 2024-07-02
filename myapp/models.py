from django.db import models

# Create your models here.
class Employe(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=30)
    salary=models.FloatField()
