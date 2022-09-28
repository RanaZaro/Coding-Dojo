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

def viewbook (request, id):
    context = {
        'book': Book.objects.get(id = int(id)),
        'authors' : Author.objects.all()

    }
    return render (request,'viewbook.html',context)
    

def authtobook (request,id):
    book1=Book.objects.get (id = int(id))
    auth1 = Author.objects.get (id = request .POST['authtobook'])
    book1.authors.add(auth1)
    return redirect ('/books/'+ str(id))





