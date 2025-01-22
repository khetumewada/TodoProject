from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todos

# Create your views here.

def list_todo_items(request):
    context = {"todo_list" : Todos.objects.all()}
    return render(request, "todos/todo.html", context)

def insert_todo_items(request:HttpRequest):
    # content = request.POST["content"]
    todos = Todos(content = request.POST["content"])
    todos.save()
    return redirect("/todos/list/")

def delete_todo_items(request, todo_id):
    todo_delete = Todos.objects.get(id = todo_id)
    todo_delete.delete()
    return redirect("/todos/list/")