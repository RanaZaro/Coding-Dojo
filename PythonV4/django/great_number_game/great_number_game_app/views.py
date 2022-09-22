from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse,redirect

import random


def method(request):
    if 'random' not in request.session:
        request.session['random']=random.randint(1, 100)
        request.session['status']=""
        request.session['guesses']= 0
    return render(request,'game.html')

def guess(request):
     
    
        if int(request.POST['guess_num']) > request.session['random']:
            request.session['status'] = 'High!'
            request.session['guesses'] += 1
              
        elif int(request.POST['guess_num']) < request.session['random']:
            request.session['status'] = 'Low!'
            request.session['guesses'] += 1
        else:
            request.session['status'] = 'Bravo!!!'
            request.session['guesses'] +=1
        
        return redirect("/")

def destroy(request):
    request.session['random']=random.randint(1, 100)
    return redirect("/")







