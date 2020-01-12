from django.shortcuts import render
from .models import ListItem
from .forms import ListItemForm

# Create your views here.

def home(request):
    all_items = ListItem.objects.all
    to_template = {'all_items': all_items}
    return render(request, "home.html", to_template)

def about(request):
    to_template = {'about_text': "This site belongs to Chris Torok"}
    return render(request, "about.html", to_template)

# end
