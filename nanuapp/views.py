from django.shortcuts import render,redirect
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def index(request):
    try:
        video_url = '/media/videos/about_office_staff.mp4'
        return render(request, 'nanuapp/index.html',{'active_page':'home','video_url': video_url})
    except:
          raise Http404()

def about(request):
    try:
            return render(request, 'nanuapp/about.html',{'active_page':'about'})
    except:
            raise Http404() # if DEBUG=False, this will render 404.html

def portfolio(request):
    try:
            return render(request, 'nanuapp/portfolio.html',{'active_page':'portfolio'})
    except:
            raise Http404()

def standard_project(request):
    try:
            return render(request, 'nanuapp/standard-project.html',{'active_page':'portfolio'})
    except:
            raise Http404()

def blog(request):
    try:
            return render(request, 'nanuapp/blog.html',{'active_page':'blog'})
    except:
            raise Http404()

def contact(request):
    try:
        if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                        name = form.cleaned_data['name']
                        sender_email = form.cleaned_data['email']
                        subject = form.cleaned_data['subject']
                        message = form.cleaned_data['message']
                              
                        # Send email
                        send_mail(
                                f'from {name} {sender_email} {subject}',
                                message,
                                sender_email,
                                recipient_list=[settings.EMAIL_HOST_USER],
                                fail_silently=False,
                        )
                return redirect('contact')  # Redirect to a new URL after POST
        else:
              form = ContactForm()
        return render(request, 'nanuapp/contact.html', {'active_page':'contact','form': form})

    except:
        raise Http404()
