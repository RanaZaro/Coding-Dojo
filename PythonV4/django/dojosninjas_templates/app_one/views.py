from multiprocessing import context
from django.shortcuts import render,redirect
from . import models

# Create your views here.
def index(request):
    context={
        "All_Dojos":models.show_dojos(),
    }
    return render (request,"index.html",context)

def Dojo(request):
    dojo_name = request.POST["name"]
    dojo_city= request.POST["city"]
    dojo_state = request.POST["state"]
    models.add_dojo (dojo_name,dojo_city,dojo_state)
    return redirect ("/")

def Ninja(request):
    ninja_first_name = request.POST["first_name"]
    ninja_last_name = request.POST ["last_name"]
    ninja_select_dojo = request.POST["select_dojo"]
    models.add_ninja(ninja_first_name, ninja_last_name, ninja_select_dojo)
    return redirect ("/")