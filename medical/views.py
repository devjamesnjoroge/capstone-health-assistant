from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def index(request):
    if request.user.username:
        return redirect('/dashboard/')

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
        return redirect('/auth/login/')

    return render(request, 'authentication/register.html')


@login_required(login_url='/auth/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/auth/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/auth/login/')
def history(request):
    if MedicalHistory.objects.filter(user=request.user).exists():
        medical_history = MedicalHistory.objects.filter(user=request.user).all()
    else:
        medical_history = None
    return render(request, 'history.html', {'medical_history': medical_history})

@login_required(login_url='/auth/login/')
def diet(request):
    if Diet.objects.filter(user=request.user).exists():
        diets = Diet.objects.filter(user=request.user).all()
    else:
        diets = None
    return render(request, 'diet.html', {'diets': diets})

@login_required(login_url='/auth/login/')
def posts(request):
    if Post.objects.all():
        posts = Post.objects.all()
    else:
        posts = None
    return render(request, 'posts.html', {'posts': posts})

@login_required(login_url='/auth/login/')
def create_profile(request):
    if  Profile.objects.filter(user=request.user).exists():
        return render(request, 'errors/403.html')
    else:
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

@login_required(login_url='/auth/login/')
def create_medical_history(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            medical_history = form.save(commit=False)
            medical_history.user = request.user
            medical_history.save()
            return redirect('/history/')
    else:
        form = MedicalHistoryForm()
    return render(request, 'forms/create_medical_history.html', {'form': form})


@login_required(login_url='/auth/login/')
def create_diet(request):
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            diet = form.save(commit=False)
            diet.user = request.user
            diet.save()
            return redirect('/diet/')
    else:
        form = DietForm()
    return render(request, 'forms/create_diet.html', {'form': form})


@login_required(login_url='/auth/login/')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/posts/')

    else:
        form = PostForm()
    return render(request, 'forms/create_post.html', {'form': form})
