from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .models import Task
# Create your views here.


class ToDoListView(ListView):
    queryset = Task.objects.all()
    template_name = 'to_do_list_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(ToDoListView, self).dispatch(request, *args, **kwargs)


class TaskView(DetailView):
    queryset = Task.objects.all()
    template_name = 'task.html'

    def dispatch(self, request, *args, **kwargs):
        return super(TaskView, self).dispatch(request, *args, **kwargs)


class CreateTask(CreateView):
    template_name = 'add_task.html'
    model = Task
    fields = ('title', 'description')
    mark_as_done = False

    def dispatch(self, request, *args, **kwargs):
        return super(CreateTask, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateTask, self).get_context_data(**kwargs)
        context['mark_as_done'] = False
        return context

    def form_valid(self, form):
        form.instance.mark_as_done = False
        return super(CreateTask, self).form_valid(form)

    def get_success_url(self):
        return reverse("to_do_list:task", args=(Task.objects.all().count(),))


class UpdateTask(UpdateView):
    template_name = 'edit_task.html'
    model = Task
    fields = ('title', 'description')

    def get_success_url(self):
        return reverse("to_do_list:task", args=(self.object.pk,))

    def dispatch(self, request, *args, **kwargs):
        return super(UpdateTask, self).dispatch(request, *args, **kwargs)


class TaskDone(UpdateView):
    template_name = 'task_done.html'
    model = Task
    fields = ('mark_as_done',)

    def get_success_url(self):
        return reverse("to_do_list:task", args=(self.object.pk,))

    def dispatch(self, request, *args, **kwargs):
        return super(TaskDone, self).dispatch(request, *args, **kwargs)