from django.db import models
from datetime import datetime
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20 , blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)



class Class(models.Model):
    class_name =  models.CharField(max_length=20 , blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.class_name)


from datetime import date


class Student(models.Model):
    name = models.CharField(max_length=20 , blank=True,null=True)
    date_of_birth = models.DateField()
    Class = models.ForeignKey(Class , on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.name)
