from django.contrib import admin
from django.urls import path
from . import views

# path('play', views.play),

urlpatterns = [
    path('', views.gameprogress),
    path("turn/<int:address>/", views.handle_turn),
    path("play/", views.play),
    path("delete_results/", views.delete_results)
]
