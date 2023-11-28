from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
#from django.contrib.auth import login
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #login(request, user)
            return redirect('home')  # Redirect to the home page or any desired page
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = SignUpForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change 'home' to the URL you want to redirect to after login
    else:
        form = SignUpForm()
    return render(request, 'login.html', {'form': form})
