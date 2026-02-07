from django.shortcuts import render,redirect,get_object_or_404
from .models import Task

# Create your views here.
def home(request):
    if request.method=='POST':
        print("POST DATA:",request.POST)
        title=request.POST.get('title')
        print("TITLE:",title)

        if title:
            Task.objects.create(title=title)
            return redirect('/')
        
    tasks=Task.objects.all()
    return render(request,'todo.html',{'tasks':tasks})

def delete_task(request, task_id):
    task=get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect("/")
