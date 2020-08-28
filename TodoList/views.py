from django.shortcuts import render,HttpResponse
from TodoList.models import Task


# Create your views here.
def home(request):
    context = {'success' : False, 'name': 'Nan'}
    if request.method == "POST":
         #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success' : True }

    return render(request, 'index.html', context)

def task(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskTitle)
    context = {'tasks' : allTasks}
    return render(request, 'task.html', context)