import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Ts
from .forms import TsForm
# Create your views here.
def index(request):
    days = [(datetime.datetime.now() + datetime.timedelta(days=i)).date() for i in range(7)] 
    tasks = Ts.objects.filter(date__gte=datetime.datetime.now())
    return render(request, 'todo/index.html', {'days': days, 'tasks': tasks})

def add_task(request: HttpRequest, date_str):
    form = TsForm({'date': date_str})
    if request.method == 'POST':
        task = TsForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('task:index')
        else:
            form = task
    return render(request, 'todo/add.html', {'form': form})
