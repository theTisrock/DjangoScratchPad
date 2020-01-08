from django.shortcuts import render

# Create your views here.

def app_three(request):
    return render(request, "app_three.html", {})

# end
