from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# タスク一覧
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    # 検索
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # 絞り込み
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # 並び替え
    sort = request.GET.get('sort')
    if sort == 'title':
        tasks =tasks.order_by('title')
    elif sort == 'due_date':
        tasks = tasks.order_by('due_date')

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'query': query,
        'status_filter': status_filter,
    })

# タスク新規作成
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'タスクを作成しました。')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'is_edit': False,
        })

# タスク詳細
@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

# タスク編集
@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'タスクを編集しました。')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'is_edit': True,
        })

# タスク削除
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, 'タスクを削除しました。')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})