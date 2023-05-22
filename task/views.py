import datetime
from typing import Any, Dict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Ts
from .forms import TsForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView


# TsList ->
# def index(request):
#     days = [(datetime.datetime.now() + datetime.timedelta(days=i)).date() for i in range(7)]
#     tasks = Ts.objects.filter(date__gte=datetime.datetime.now())
#     return render(request, 'task/index.html', {'days': days, 'tasks': tasks})

# AddTask
# def add_task(request: HttpRequest, date_str):
#     form = TsForm({'date': date_str})
#     if request.method == 'POST':
#         task = TsForm(request.POST)
#         if task.is_valid():
#             task.save()
#             return redirect('task:index')
#         else:
#             form = task
#     return render(request, 'task/add.html', {'form': form})

class TsList(ListView):
    template_name = 'task/index.html'
    context_object_name = "tasks"
    queryset = Ts.objects.filter(date__gte=datetime.datetime.now()).order_by('pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['days'] = [(datetime.datetime.now() + datetime.timedelta(days=i)).date() for i in range(7)]
        return context


class TaskDetail(DetailView):
    model = Ts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddTask(FormView):
    template_name = 'task/add.html'
    form_class = TsForm
    success_url = reverse_lazy('task:index')

    def get_initial(self):
        initial = {'done': Ts.Done.NOT, 'date': self.kwargs['date_str']}
        return initial

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['date'] = self.kwargs['date_str']
        return context
    
class TaskChange(UpdateView):
    model = Ts
    form_class = TsForm
    template_name = 'task/ts_form.html'
    success_url = reverse_lazy('task:index')


class TaskDelete(DeleteView):
    model =Ts
    success_url = reverse_lazy('task:index')
    template_name = 'task/task_delete.html'


def done_change(request, pk_task):
    cur_task = Ts.objects.get(pk=pk_task)
    
    if cur_task.done == Ts.Done.DONE:
        cur_task.done = Ts.Done.NOT
    else:
        cur_task.done = Ts.Done.DONE

    cur_task.save()
    return redirect('task:index')
