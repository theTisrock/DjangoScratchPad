from django.shortcuts import render

# Create your views here.

def app_three(request):
    to_template = {'app_three_text': "Welcome to App 3 Root"}
    return render(request, "app_three.html", to_template)

# end
