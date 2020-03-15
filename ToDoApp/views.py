# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Todo


# @csrf_exempt
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'ToDoApp/index.html', {'todo_items': todo_items})


def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    length_of_index = Todo.objects.all().count()
    return HttpResponseRedirect('/')
    
def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
    

