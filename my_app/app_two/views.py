from django.shortcuts import render

# Create your views here.

def app_two(request):
    return render(request, "app_two.html", {})



# end
