from .views import *
from django.contrib import admin
from django.urls import path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'index'),
    path('todo/',TodoListView.as_view(),name='todo-list'),
    path('todo/create/',TodoCreateView.as_view(),name='todo-create'), 
    path('todo/<int:pk>/delete/',TodoDeleteView.as_view(),name='todo-delete'),
    path('todo/<int:pk>/edit/',TodoEditView.as_view(),name='todo-edit'),  
    path('signup/', signup, name = 'signup'),
    path('loginn/',loginn, name = 'login'),
    path('signout/',signout, name='signout'),
    
]