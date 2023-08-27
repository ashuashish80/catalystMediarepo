from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_view(request):
    if request.method=="POST":
        UserName=request.POST['UserName']
        Password=request.POST['Password']
        user = authenticate(username=UserName, password=Password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('usename and passord incorrect')
    return render(request, 'login.html')

def Registration(request):
    if request.method=="POST":
        UserName = request.POST["UserName"]
        email = request.POST["email"]
        Password = request.POST["Password"]
        Password1 = request.POST["Password1"]
        # print(UserName,email,Password,Password1)
        signup_user = User.objects.create_user(UserName, email, Password)
        signup_user.save()
        return HttpResponse("user Created you may log in")
    else:
        return render(request, 'Registration.html')
    
    return render(request, 'Registration.html')
@login_required(login_url='login_view')
def home(request):
    return render(request, 'home.html')

def logoutpage(request):
    logout(request)
    return redirect('login_view')

def changepass(request):
    u = User.objects.get(username='UserName')
    u.set_password('new password')
    u.save()
