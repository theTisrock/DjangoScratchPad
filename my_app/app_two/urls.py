from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.app_two, name='app_two'),
]
