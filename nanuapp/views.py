from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
    try:
            return render(request, 'nanuapp/index.html')
    except:
            raise Http404()

def about(request):
    try:
            return render(request, 'nanuapp/about.html')
    except:
            raise Http404() # if DEBUG=False, this will render 404.html

def portfolio(request):
    try:
            return render(request, 'nanuapp/portfolio.html')
    except:
            raise Http404()

def blog(request):
    try:
            return render(request, 'nanuapp/blog.html')
    except:
            raise Http404()

def contact(request):
    try:
            return render(request, 'nanuapp/contact.html')
    except:
            raise Http404()

