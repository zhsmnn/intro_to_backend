from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import TodoForm
from .serializers import TodoSerializer


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')


@api_view(['GET'])
def api_todo_list(request):
    """
    Получить список всех задач
    """
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_todo_detail(request, id):
    """
    Получить подробности о задаче по ID
    """
    todo = get_object_or_404(Todo, id=id)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)

@api_view(['POST'])
def api_todo_create(request):
    """
    Создать новую задачу
    """
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_todo_delete(request, id):
    """
    Удалить задачу по ID
    """
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, "todos/index.html")