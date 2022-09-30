from django.shortcuts import render , redirect, HttpResponse
from time import gmtime, strftime
from .models import Show
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index2 (request):
    return redirect ('/shows')

def index(request):
    context = {
        "shows" :Show.objects.all(),

    }
    return render (request, 'index.html', context)

def new (request):
    return render (request,'create.html')

def edit (request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id)
    }
    return render (request,'edit.html', context)

def show(request,show_id):
    context = {
        "this_show" : Show.objects.get(id=show_id)
    }
    return render (request,'show.html',context)

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key , value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        c = Show.objects.create(title=request.POST['title'],network = request.POST['network'],release_date = request.POST['release_date'], description= request.POST['description'])
    return redirect (f'/shows/{c.id}')

def update (request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,Value in errors.items():
            messages.error(request, Value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        update = Show.objects.get(id=show_id)
    update.title = request.POST['title'] 
    update.network = request.POST['network']
    update.release_date = request.POST['release_date']
    update.description = request.POST['description']
    update.save()
    return redirect (f'/shows/{show_id}')

def delete (request, show_id):
    showsgone = Show.objects.get(id=show_id)
    showsgone.delete()
    return redirect('/shows')
