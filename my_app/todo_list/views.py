from django.shortcuts import render, redirect
from .models import ListItem
from .forms import ListItemForm, EditItemForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):

    edit_mode = False

    if request.method == 'POST':
        form = ListItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item added :)"))
            to_template = {'all_items': ListItem.objects.all}
            to_template['edit_mode': edit_mode]
            return render(request, 'home.html', to_template)

    else:
        to_template = {'all_items': ListItem.objects.all}
        to_template['edit_mode': edit_mode]
        return render(request, 'home.html', to_template)

def about(request):
    to_template = {'about_text': "This site belongs to Chris Torok"}
    return render(request, "about.html", to_template)

def delete(request, list_id):
    item = ListItem.objects.get(pk=list_id)
    item.delete()
    messages.success(request, (f"item {list_id} deleted"))
    return redirect('home')

def toggle(request, list_id):
    item = ListItem.objects.get(pk=list_id)

    item.complete = False if item.complete == True else True
    item.save()

    return redirect('home')

def edit(request, list_id: int):

    # click save
    if request.method == 'POST':
        form = EditItemForm(request.POST or None)
        
        if form.is_valid():
            # TODO update in db
            new_item_name = form.data[f'item{list_id}']
            item = ListItem.objects.get(pk=list_id)
            item.item = new_item_name
            item.save()
            messages.success(request, (f"item {list_id} updated"))
            return redirect('home', )

    # click edit
    else:
        to_template = ListItem.objects.all
        to_template['edit_mode'] = True
        return render(request, 'home.html', to_template)

    pass

# end
