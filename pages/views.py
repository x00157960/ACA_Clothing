from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from shop.views import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
