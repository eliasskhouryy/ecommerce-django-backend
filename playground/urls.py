from django.urls import path
from . import views

#URLCong or URL configuration
urlpatterns = [
    path('hello/', views.say_hello)
]