from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("other-route/", views.other_route, name="other_route_name"),
    path("spectate", views.spectate, name="spectate"),
]
