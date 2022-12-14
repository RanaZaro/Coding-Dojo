from django.shortcuts import render,redirect
import random
from datetime import datetime
def method(request):
    if 'count' not in request.session:
        request.session['count']= 0
    if 'activities' not in request.session:
        request.session['activities'] = []
       

    return render(request,"ninjagold.html")

def process_money(request):
    now = datetime.now().strftime('%B %d %Y, %I:%M %p ')
    if request.POST['button'] == "farm":
        gold = random.randint(10,20)
        request.session['count'] += gold
        activity = "You entered a farm and earn " +" "+ str(gold) + " " +"gold." +" " +"(" + str(now) +")"
        request.session['activities'].append(activity)
    elif request.POST['button'] == "cave":
        gold = random.randint(10,20)
        request.session['count'] += gold
        activity = "You entered a cave and earn " +" " + str(gold) + " " +"gold." +" "  +"(" + str(now) +")"
        request.session['activities'].append(activity)
    elif request.POST['button'] == "house":
        gold = random.randint(10,20)
        request.session['count'] += gold
        activity = "You entered a house and earn " + " " + str(gold) + " "  +"gold." +" " +"(" + str(now) +")"
        request.session['activities'].append(activity)
    elif request.POST['button'] == "quest":
        gold = random.randint(-50,50)       
        if gold >0:

            request.session['count'] += gold
            activity = "You entered a quest and earn " +" " + str(gold) + " " +"gold." +" "+"("  +  str(now) +")"
            request.session['activities'].append(activity)
        elif gold<0:
            request.session['count'] -= gold
            activity = "You failed a quest and lost " +" " + str(gold) + " " +"gold." +"Ouch." + "("  +  str(now) +")"
            request.session['activities'].append(activity)
    return redirect('/')

def reset(request):
    request.session['count']=0
    request.session['activities']=[]

    return redirect('/')

