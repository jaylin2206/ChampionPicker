from django.urls import path

from . import views

app_name = "champions"

urlpatterns = [
    path("", views.index, name="index"),
    path("champion/<str:name>", views.champion, name="champion"),
]
