from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Aman is great",
    }
    return render(request, 'index.html', context )
    #return HttpResponse("this is Home page")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is About page")
def service(request):
    return render(request, 'service.html')
    #return HttpResponse("this is Service page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        name = request.POST.get('name')
        contact = Contact(name=name, email=email, phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been send")
    return render(request, 'contact.html')
    #return HttpResponse("this is Contact page")
