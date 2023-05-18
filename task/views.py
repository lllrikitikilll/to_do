import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Ts
from .forms import TsForm
# Create your views here.
def index(request):
    today = Ts.objects.filter(date=datetime.datetime.now())
    tomorrow = Ts.objects.filter(date=datetime.datetime.now() + datetime.timedelta(days=1))

    return render(request, 'todo/index.html', {'today': today,
                                               "tomorrow": tomorrow})

def add_task(request: HttpRequest):
    form = TsForm()
    if request.method == 'POST':
        task = TsForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('task:index')
        else:
            form = task
    return render(request, 'todo/add.html', {'form': form})
