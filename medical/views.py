from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def index(request):
    if request.user.username:
        return redirect('/home/')

    return render(request, 'index.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        return redirect('/')

    return render(request, 'authentication/register.html')

@login_required(login_url='/auth/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/auth/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/auth/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/auth/login/')
def history(request):
    return render(request, 'history.html')

@login_required(login_url='/auth/login/')
def diet(request):
    return render(request, 'diet.html')

@login_required(login_url='/auth/login/')
def posts(request):
    return render(request, 'posts.html')

@login_required(login_url='/auth/login/')
def create_profile(request):
    if request.user.profile:
        return render(request, 'errors/403.html')
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/profile/')
    else:
        form = ProfileForm()
    return render(request, 'forms/create_profile.html', {'form': form})
