from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from SRC.models import Image
from SRC.forms import RegisterForm, AddImage
from django.template import loader



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'me',
            'year':datetime.now().year,
        }
    )

def images(request):
    images = Image.objects.filter()
    context = {'images': images,
               'year': datetime.now().year,
               'title':'Images',
               'message': 'GPZ INDUSTRIEZZZ COLLECTION'}
    return render(
        request,
        'app/images.html',
        context=context,

    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
    return render(
        request,
        'app/signup.html',
        {'form': form,
         'year': datetime.now().year,
         },
    )

def addimage(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/images/')
    else:
        form = AddImage()
    return render(
        request,
        'app/addimage.html',
        {'form': form,
        'title':'Add image',
        'year': datetime.now().year,
        }
    )