from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return str(self.name) 

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) 
