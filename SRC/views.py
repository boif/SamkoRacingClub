from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from SRC.models import Image
from SRC.forms import RegisterForm, AddImage



def home(request):
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
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'year':datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )

def images(request):
    assert isinstance(request, HttpRequest)
    images = Image.objects.filter()
    return render(
        request,
        'app/images.html',
        {'images': images,
         'year': datetime.now().year,
         'title': 'Images',
         'message': 'GPZ INDUSTRIEZZZ COLLECTION'}

    )

def register(request):
    assert isinstance(request, HttpRequest)
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

def profile(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profile.html',
        {
            'title': 'Your profile',
            'year': datetime.now().year,
        }
    )
