from django.shortcuts import render
from .models import Contact

def home(req):
    context = {
        'title': 'Home'
    }
    return render(req, 'home.html', context)


def product(req):
    context = {
        'title': 'Products'
    }
    return render(req, 'product.html', context)

def service(req):
    context = {
        'title': 'Services'
    }
    return render(req, 'service.html', context)

def about(req):
    context = {
        'title': 'Contact'
    }
    return render(req, 'about.html', context)


def contact(req):
    context = {
        'title': 'Contact'
    }
    if req.method == 'POST':
        contact = Contact(
            name=req.POST['name'], 
            email= req.POST['email'],
            subject = req.POST['subject'],
            message = req.POST['message']
        )
        contact.save()

    return render(req, 'contact.html', context)
