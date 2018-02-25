from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .models import Task, User
# Create your views here.


class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    success_url = '/login/'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save(commit=True)
        return super(CreateUser, self).form_valid(form)


def register(request):
    if request.method == 'GET':
        form = CreateUser()
    else:
        form = CreateUser(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/login/')
    return render(request, 'register.html', {'form': form})


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
        form.instance.author = self.request.user
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

    def get_queryset(self):
        return super(UpdateTask, self).get_queryset().filter(author=self.request.user)


class TaskDone(UpdateView):
    template_name = 'task_done.html'
    model = Task
    fields = ('mark_as_done',)

    def get_success_url(self):
        return reverse("to_do_list:task", args=(self.object.pk,))

    def dispatch(self, request, *args, **kwargs):
        return super(TaskDone, self).dispatch(request, *args, **kwargs)