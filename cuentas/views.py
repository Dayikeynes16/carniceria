from django.shortcuts import render

def index(request):
   
    return render(request, 'hola.html' )

def imagen(request):
    return ('images/B_4.png')