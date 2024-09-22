from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    #return HttpResponse('Home page')
    content = {}
    return render(request, 'webapp/index.html', content)
    
    
# Login a user
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            
            if user is not None:
               auth.login(request, user)
               return redirect('dashboard')
            
    context = {'form':form}
    return render(request, 'webapp/login.html', context)
    
    
def register_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #user = form.save(commit=False)
            #user.username = user.username.lower()
            form.save()
    
            return redirect('login-user')
    context = {'form':form}
    return render(request, 'webapp/register.html', context)

def logoutUser(request):
    auth.logout(request)
    #messages.info(request, 'Logout Successful ')
    return redirect('login')

def updateRecord(request):
    context = {}
    return render(request, 'webapp/update-record.html', context)

def createRecord(request):
    context = {}
    return render(request, 'webapp/create-record.html', context)

def viewRecord(request):
    context = {}
    return render(request, 'webapp/view-record.html', context)



@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'webapp/dashboard.html', context)
    
   
    
    
    
    
    
    
    
    
    