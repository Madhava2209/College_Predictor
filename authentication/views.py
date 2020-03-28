from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST["user"]
        Email=request.POST["email"]
        Password=request.POST["password"]
        user=User.objects.create_user(username=username,email=Email,password=Password)
        login(request,user)
        return redirect("/get_rank/")

    return render(request,"signup.html")


def user_login(request):
    context = {}
    if request.method=="POST":
        username =request.POST['username']
        password =request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/get_rank/')
        else:
            context['error']="Provide valid credentials!!"
            return render(request,'login.html',context)
    else:
        return render(request,'login.html',context)


def success(request):
    if request.user.is_authenticated:
        context = {}
        context["user"]=request.user
        return render(request,'success.html',context)
    else:
        return redirect('/login/')


def user_logout(request):
        logout(request)
        return redirect('/home/')
