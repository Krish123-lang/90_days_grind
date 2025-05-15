from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('post/post_detail/<int:id>', views.post_detail, name='post_detail'),
    path('post/edit/<int:id>', views.edit, name='edit'),
    path('post/delete/<int:id>', views.delete, name='delete'),
]
