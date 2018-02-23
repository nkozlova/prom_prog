from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from views import ToDoListView, TaskView, CreateTask, UpdateTask, done_task


urlpatterns = [
    url(r'^$', ToDoListView.as_view(), name="to_do_list_list"),
    url(r'^(?P<pk>\d+)/$', TaskView.as_view(), name="task"),
    url(r'^new/$', login_required(CreateTask.as_view()), name="add_task"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateTask.as_view()), name="edit_task"),

    url(r'^(?P<pk>\d+)/done/task$', done_task, name="task_done"),
]
