from django.db import models

# Create your models here.
# class My_Model(models.Model):gg



class My_Model(models.Model):
    name = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    