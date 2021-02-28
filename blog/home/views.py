from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable" : "Jai Dhingra"
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message hs been sent")

    return render(request, 'contact.html')
    

def services(request):
    return render(request, 'services.html')
    

def about(request):
    
    return render(request, 'about.html')
    