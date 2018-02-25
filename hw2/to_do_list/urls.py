from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.ToDoListView.as_view(), name="to_do_list_list"),
    url(r'^(?P<pk>\d+)/$', views.TaskView.as_view(), name="task"),
    url(r'^new/$', login_required(views.CreateTask.as_view()), name="add_task"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(views.UpdateTask.as_view()), name="edit_task"),
    url(r'^(?P<pk>\d+)/done/$', login_required(views.TaskDone.as_view()), name="task_done"),
]
