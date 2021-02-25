from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "Jai Dhingra"
    }
    return render(request, 'index.html', context)

def contact(request):
    return HttpResponse("Contact Us")

def services(request):
    return HttpResponse("Services")

def about(request):
    return HttpResponse("About Us")