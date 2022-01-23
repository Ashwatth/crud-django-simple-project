from django.db import models
class company(models.Model):
    cpnname=models.CharField(max_length=100)
    cpnjob=models.CharField(max_length=100)
    cpnsalary=models.CharField(max_length=100)
    