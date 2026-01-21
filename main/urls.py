from django.urls import path
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("generate-link/", views.generate_link, name="generate"),
        path("<str:link>/", views.call_url, name="call_url"),
        ]
