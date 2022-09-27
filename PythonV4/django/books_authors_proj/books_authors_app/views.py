from django.shortcuts import render, redirect
from . models import *

# Create your views here.
def index (request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'form.html', context)

def addbook (request):
    Book.objects.create(title=request.POST['title'])
    return redirect ('/')





