from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/create", views.create_post, name="create_post"),
    path("post/edit/<int:id>", views.edit_post, name="edit_post"),
    path("about", views.about, name="about"),
]
