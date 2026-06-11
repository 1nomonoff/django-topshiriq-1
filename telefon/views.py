from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def telefon(request):
    return HttpResponse("Telefon narxi 1000$")
