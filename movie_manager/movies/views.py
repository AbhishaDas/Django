from turtle import title
from django.shortcuts import render, redirect
from . models import movie_info
from . forms import MovieForm, ModelForm

# Create your views here.
def create(request):
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('list')  
    else:
        frm = MovieForm()
        
    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_details = movie_info.objects.all()
    print(movie_details)
    return render(request,'list.html',{'movies' :movie_details})

def edit(request,pk):
    editing_instance = movie_info.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=editing_instance)
        if frm.is_valid():
            editing_instance.save()
            
        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # summary=request.POST.get('summary')
        # editing_instance.title=title
        # editing_instance.year=year
        # editing_instance.summary=summary
        # editing_instance.save()
    else:        
        frm=MovieForm(instance=editing_instance)
        
    return render(request,'create.html',{'frm':frm})
 
def delete(request,pk):
    instance = movie_info.objects.get(pk=pk)
    instance.delete()
    movie_details = movie_info.objects.all()
    return render(request,'list.html',{'movies' :movie_details})
 

 