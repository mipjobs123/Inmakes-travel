from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
       uname=request.POST['username']
       pwd=request.POST['password']
       user=auth.authenticate(username=uname,password=pwd)

       if user is not None:
           auth.login(request,user)
           return redirect('/')     # to home page
       else:
           messages.info(request,"invalid credentials")
           return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
       uname=request.POST['username']
       fname = request.POST['first_name']
       lname = request.POST['last_name']
       Email = request.POST['email']
       PASSWORD = request.POST['password']
       Cpassword= request.POST['password1']
       if PASSWORD==Cpassword:
           if User.objects.filter(username=uname).exists():
               messages.info(request,"username already used")
               return redirect('register')
           elif User.objects.filter(email=Email).exists():
               messages.info(request, "email already used")
               return redirect('register')
           else:
                user=User.objects.create_user(username=uname,password=PASSWORD,first_name=fname,last_name=lname,email=Email)
                user.save()
                return redirect('login')
                print("user created")

       else:
            messages.info(request,"password not match")
            return redirect('register')
       return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')