from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.app_three, name='app_three'),
]

# end
