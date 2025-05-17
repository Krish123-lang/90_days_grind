from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('api/', include(router.urls)),
]