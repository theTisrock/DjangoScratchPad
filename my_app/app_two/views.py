from django.shortcuts import render

# Create your views here.

def app_two(request):
    to_template = {'app_two_text': "Welcome to the App 2 Root"}
    return render(request, "app_two.html", to_template)



# end
