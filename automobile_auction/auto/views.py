from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class HomePage(TemplateView):
    template_name = 'homepage.html'

class AboutUs(TemplateView):
    template_name = 'aboutus.html'

class SearchDatabase(TemplateView):
    template_name = 'searchdatabase.html'

class LogIn(TemplateView):
    template_name = 'login.html'