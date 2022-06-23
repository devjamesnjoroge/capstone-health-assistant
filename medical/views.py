from django.shortcuts import redirect, render
from django.contrib.auth.models import User

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


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def history(request):
    return render(request, 'history.html')

def diet(request):
    return render(request, 'diet.html')

def posts(request):
    return render(request, 'posts.html')
