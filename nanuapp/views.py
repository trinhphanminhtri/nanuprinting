from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'nanuapp/index.html')

def about(request):
    return render(request, 'nanuapp/index.html')

def services(request):
    return render(request, 'nanuapp/index.html')

def contact(request):
    return render(request, 'nanuapp/index.html')

