from django.urls import path
from .views import todo_list, todo_create, todo_delete, todo_detail

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('todo_list/<int:pk>/', todo_detail, name='todo_detail'),
    path('create/', todo_create, name='todo_create'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
]
