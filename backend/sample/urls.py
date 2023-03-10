from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('getTodo/', views.getTodo, name="getTodo")
]
