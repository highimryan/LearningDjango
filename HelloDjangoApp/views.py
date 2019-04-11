from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def index(request):
    now = datetime.now()
    # displays tab title
    html_content = "<html><head><title>Learning Django</title></head><body>"
    # displays the words Hello, Django! + the current time
    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"
    # returns the above html content
    return HttpResponse(html_content)

# Create your views here.
