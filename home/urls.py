from django.urls import path
from . import views

urlpatterns = [
    path("authorized", views.Authorized.as_view()),
    path("home", views.HomeView.as_view())
]
