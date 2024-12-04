"""
URL configuration for ToDoListProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Tasks.views import getTasks, getDetails, addTask, updateTask, deleteTask, getCategories, addCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getall/', getTasks.as_view(), name='get all'),
    path('get/<int:pk>' , getDetails.as_view(), name='get'),
    path('newtask/', addTask.as_view(), name='new task'),
    path('edittask/<int:pk>', updateTask.as_view(), name='edit task'),
    path('deletetask/<int:pk>', deleteTask.as_view(), name='delete task'),
    path('categories/', getCategories.as_view(), name='get categories'),
    path('addcategory/', addCategory.as_view(), name='add category'),
]
