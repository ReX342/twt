from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"),
    #path("<int:id>", views.index, name="index"),
    #path("", views.home, name="home")
]
