from django.db import models

# Create your models here.
class Dojo (models.Model):
    name=models.CharField (max_length = 45)
    city= models.CharField (max_length= 45)
    state = models.CharField(max_length=45)

class Ninja (models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojo=models.ForeignKey(Dojo,related_name="ninjas",on_delete=models.CASCADE)


def show_dojos():
    return Dojo.objects.all()

def add_dojo (dojo_name,dojo_city,dojo_state):
    Dojo.objects.create(name=dojo_name, city=dojo_city,state=dojo_state)

def add_ninja(ninja_first_name,ninja_last_name,ninja_select_dojo):
    Ninja.objects.create(first_name=ninja_first_name,last_name=ninja_last_name,dojo=Dojo.objects.get(name=ninja_select_dojo) )

