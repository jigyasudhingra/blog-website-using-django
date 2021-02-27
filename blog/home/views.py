from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "Jai Dhingra"
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
    

def services(request):
    return render(request, 'services.html')
    

def about(request):
    return render(request, 'about.html')
    