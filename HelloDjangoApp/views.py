from django.shortcuts import render
from django.http import HttpResponse
# imports a datetime
from datetime import datetime

# Create your views here


def index(request):
    now = datetime.now()

    return render(
        request,
        # Relative path from the 'templates' folder to the template file
        "HelloDjangoApp/index.html",
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title': "Hello Django",
            'message': "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )


def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title': "About HelloDjangoApp",
            'content': "Example app page for Django."
        }
    )
