from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class IndexView(TemplateView):
    template_name = 'iflogout/index.html'

class HomePage(TemplateView):
    template_name = 'iflogout/homepage.html'

class AboutUs(TemplateView):
    template_name = 'iflogout/aboutus.html'

class SearchDatabase(TemplateView):
    template_name = 'iflogout/searchdatabase.html'

class AddCar(TemplateView):
    template_name = 'iflogout/addcar.html'

class LogHomePage(TemplateView):
    template_name = 'iflogin/loghomepage.html'

class LogAboutUs(TemplateView):
    template_name = 'iflogin/logaboutus.html'

class LogSearchDatabase(TemplateView):
    template_name = 'iflogin/logsearchdatabase.html'

class LogAddCar(TemplateView):
    template_name = 'iflogin/addcar.html'

def loginUser(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, 'iflogin/logout.html')
        else:
            messages.info(request, 'Zły login lub hasło')

    context = {'form': form }
    return render(request, 'iflogout/login.html', context)

def registration(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created, welcome ' + user)
            return render(request, 'iflogout/login.html')

    context = {'form': form }
    return render(request, 'iflogout/registration.html', context)

def userLogOut(request):
    form = LoginForm()
    logout(request)
    context = {'form': form}
    return render(request, 'iflogout/login.html', context)