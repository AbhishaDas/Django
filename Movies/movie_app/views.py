from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    movie_details = {'movies' : [
    {   "title":"Aavesham",
        "year": 2024,
        "summary": "Story of Ranganna",
        "sucess": True
    },
    {   "title":"Bhramayugam",
        "year": 2024,
        "summary": "Story of Chaathan",
        "sucess": True
    },
    {   "title":"Varshagalkkushesham",
        "year": 2024,
        "sucess": True
    },
    {   "title":"Premalu",
        "year": 2024,
        "summary": "Comedy Romatic entertainment",
        "sucess": True
    },
    {   "title":"Aadujeevitham",
        "year": 2024,
        "summary": "Real Story of Najeeb",
        "sucess": True
    },
                     ]}
    return render(request,"hello.html",movie_details)
