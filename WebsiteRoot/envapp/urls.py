from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),
    path('gamekeeper/', views.gamekeeper, name='gamekeeper'),
]