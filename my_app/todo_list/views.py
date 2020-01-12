from django.shortcuts import render
from .models import ListItem

# Create your views here.

def home(request):
    to_template = {'home_text': "Welcome to the the Root!"}
    return render(request, "home.html", to_template)

def about(request):
    to_template = {'about_text': "This site belongs to Chris Torok"}
    return render(request, "about.html", to_template)

# end
