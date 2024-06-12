from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    search = request.GET.get('q')
    if search:
        todos = todos.filter(title__icontains=search)
    context = {'todos': todos}
    return render(request, 'todo_list.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    context = {'todo': todo, 'form': form}
    return render(request, 'todo_detail.html', context)


def todo_create(request):
    forms = TodoForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Todo created!')
        return redirect('/')
    else:
        forms = TodoForm()
    context = {'form': forms}
    return render(request, 'created.html', context)


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted!')
        return redirect('/')
    context = {'todo': todo}
    return render(request, 'delete.html', context)


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        redirect(request, 'todo_detail', id=pk)
        context = {'form': form}
        return render(request, 'edit.html', context)
