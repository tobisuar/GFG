from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, "authentification/index.html")

def signip(request):
    return render (request, "autentification/signup.html")
def signip(request):
    return render (request, "autentification/signin.html")
def signip(request):
    pass