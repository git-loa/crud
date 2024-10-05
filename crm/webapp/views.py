from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, LoginForm, RecordForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
#import models
from .models import Record




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
    # create a form instance
    form = CustomUserCreationForm()
    if request.method == 'POST':
        # populate it with data from the request
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #user = form.save(commit=False)
            #user.username = user.username.lower()
            form.save()
    
            return redirect('login-user')
    context = {'form':form}
    return render(request, 'webapp/register.html', context)


def logoutUser(request):
    logout(request)
    #messages.info(request, 'Logout Successful ')
    return redirect('login-user')


@login_required(login_url='login-user')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateRecord(request, pk):
    
    record = Record.objects.get(id=pk)
    
    # create a form instance
    form = RecordForm(instance=record)
    if request.method == 'POST':
        # populate it with data from the request
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form':form}
    return render(request, 'webapp/update-record.html', context)

    

@login_required(login_url='login-user')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewRecord(request, pk):
    
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request, 'webapp/view-record.html', context)



@login_required(login_url='login-user')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    
    records = Record.objects.all()
    
    context = {'records':records}
    return render(request, 'webapp/dashboard.html', context)
    
@login_required(login_url='login-user')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createRecord(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form':form}
    return render(request, 'webapp/create-record.html', context)

@login_required(login_url='login-user')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteRecord(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect("dashboard")
    
    
    
    
    
    
    