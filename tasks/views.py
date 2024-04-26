from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
from .forms import TaskForm

# Create your views here.
def index(request):
    form = TaskForm()
    tasks = task.objects.all()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {
        'tasks': tasks,
        'form' : form
    }
    return render(request, 'tasks/list.html', context)

def update_task(request,pk):
    tasks = task.objects.get(id=pk)
    form = TaskForm(instance= tasks)
    
    if request.method=="POST":
        form= TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("/")
            
    context={
        'form':form,
    }
    return render(request,'tasks/update_task.html',context)

def delete(request,pk):
    item = task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {
        'item': item,
    } 
    return render(request, 'tasks/delete.html', context)
    