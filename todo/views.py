from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AllTasks(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'all_tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_no'] = context['all_tasks'].filter(completed=False).count()
        context['count_yes'] = context['all_tasks'].filter(completed=True).count()
        context['count_all'] = context['all_tasks'].count()

        search = self.request.GET.get('searchbar') or ''
        if search:
            context['all_tasks'] = context['all_tasks'].filter(name__icontains=search)

        context['search'] = search

        return context


class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('all-tasks')
    template_name = 'create_task.html'


class EditTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('all-tasks')
    template_name = 'create_task.html'


class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('all-tasks')
    template_name = 'delete_task.html'
    context_object_name = 'task'


class DetailTask(DetailView):
    model = Task
    template_name = 'detail_task.html'
    context_object_name = 'task'
