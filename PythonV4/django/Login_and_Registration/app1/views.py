from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt   

# Create your views here.
def index(request):
    return render(request, "login_reg.html")

def create_user(request):
    if request.method == "POST":
        errors = Registration.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        password = request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)  

        user1 = Registration.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
            birthday=request.POST['birthday']
        )
        request.session['user_id'] = user1.id
        return redirect('/success')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = Registration.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0]
    }
    return render(request, 'login_succ.html', context)

def login_user(request):
    if request.method == "POST":
        errors = Registration.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = Registration.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

