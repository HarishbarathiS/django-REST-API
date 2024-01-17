from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


    def __str__(self): #string representation of an instance 
        return self.name + ' ' + self.description