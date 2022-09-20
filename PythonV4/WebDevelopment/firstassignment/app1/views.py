

from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def rana(request):
    return HttpResponse("hello World !")

