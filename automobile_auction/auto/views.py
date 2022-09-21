from django.shortcuts import render
from django.views.generic import View, TemplateView
from .forms import LoginForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class HomePage(TemplateView):
    template_name = 'homepage.html'

class AboutUs(TemplateView):
    template_name = 'aboutus.html'

class SearchDatabase(TemplateView):
    template_name = 'searchdatabase.html'

class AddCar(TemplateView):
    template_name = 'addcar.html'

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(
                request=request,
                template_name='addcar.html',
            )

    return render(
        request = request,
        template_name = 'login.html',
        context = {
            'form': form
        }
    )

def registration(request):
    form = LoginForm()
    return render(request = request, template_name = 'registration.html', context = {'form': form })