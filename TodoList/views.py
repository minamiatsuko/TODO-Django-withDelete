from django.shortcuts import render,HttpResponse,redirect
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

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Item Has Been Deleted from List!'))
    return redirect('task')