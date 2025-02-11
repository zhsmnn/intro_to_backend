from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def delete_todo(request, id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
        return redirect('todo_list')
    return HttpResponseForbidden("Direct GET request is not allowed for deletion.")
