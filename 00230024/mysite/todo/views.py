from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    task_list = Task.objects.all()
    context = {
        'tasks': task_list
    }
    return render(request, 'todo/index.html', context)


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    # return HttpResponse("success")
    return HttpResponseRedirect(reverse('todo:index'))


def add(request):
    task = Task()
    task.task_desc = request.POST['desc']
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))
    # return HttpResponse("success")

