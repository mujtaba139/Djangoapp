from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLoginView, RegisterPage,task_delete,task_complete
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'base'
urlpatterns = [
    path("login/", UserLoginView.as_view(), name='login'),
    path("register/", RegisterPage.as_view(), name='register'),
    path("logout/", LogoutView.as_view(next_page='base:login'), name='logout'),
    path("",TaskList.as_view(), name='todo'),
    path("task/<int:pk>/",TaskDetail.as_view(), name='task'),
    path("task-create/",TaskCreate.as_view(), name='task-create'),
    path("task-update/<int:pk>/",TaskUpdate.as_view(), name='task-update'),
    path("task-delete/<int:pk>/",TaskDelete.as_view(), name='task-delete'),
    path("task_delete/",views.task_delete, name='task_delete'),
    path("task_complete/",views.task_complete, name='task_complete'),
    
]