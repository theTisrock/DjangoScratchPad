from django.shortcuts import render
from .models import ListItem
from .forms import ListItemForm
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item added :)"))
            to_template = {'all_items': ListItem.objects.all}
            return render(request, 'home.html', to_template)

    else:
        to_template = {'all_items': ListItem.objects.all}
        return render(request, 'home.html', to_template)

def about(request):
    to_template = {'about_text': "This site belongs to Chris Torok"}
    return render(request, "about.html", to_template)

# end
