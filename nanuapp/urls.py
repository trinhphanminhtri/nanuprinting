from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('about/', views.about, name='about'), 
    path('portfolio/', views.portfolio, name='portfolio'), 
    path('standard-project/', views.standard_project, name='standard-project'),
    path('blog/', views.blog, name='blog'), 
    path('contact/', views.contact, name='contact'), 
]