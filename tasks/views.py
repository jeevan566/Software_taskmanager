from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

# home function
def home(request):
    return render(request, 'tasks/home.html')

# task list functions (login required)
@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# task creation functions (login required)
@login_required
def create_task(request, task_id=None):
    task = get_object_or_404(Task, pk=task_id) if task_id else None
   

    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        project = request.POST.get('project')

        if task:
            task.title = title
            task.name = name
            task.description = description
            task.due_date = due_date
            task.priority = priority
            task.status = status
            task.project = project
            task.save()
        else:
            Task.objects.create(
                title=title,
                name = name,
                description=description,
                due_date=due_date,
                priority=priority,
                status=status,
                project=project,
                user=request.user,
    
            )
        return redirect('task_list')

    return render(request, 'tasks/create_task.html', {'task': task})


# register functions (login required)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})


# login functions 
@login_required
@user_passes_test(lambda user: user.is_superuser)
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.project = request.POST.get('project')
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/create_task.html', {'task': task})

# delete functions (login required)
@login_required
@user_passes_test(lambda user: user.is_superuser)
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

# Dashboard (Login required)
@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()  # Admin sees all tasks
    else:
        tasks = Task.objects.filter(user=request.user)  # Standard user sees only their tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
