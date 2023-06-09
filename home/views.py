from django.shortcuts import render
from django.http import HttpResponse
people=[
        {'name':'santo','age':25},
        {'name':'leo','age':24}
    ]

def home(request):
   
    return render(request,"index.html",context ={'people':people })

def contact(request):
    return render(request,"contact.html",context ={'people':people })