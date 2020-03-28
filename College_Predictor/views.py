from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from College_Predictor.models import College

from django.db.models import Q

# Create your views here.


def home(request):
    return render(request,"home.html")




def add_college(request):
    user=request.user
    if user.is_staff:

        if request.method=="POST":
            college_name=request.POST["college_name"]
            college_id=request.POST["college_id"]
            location=request.POST["location"]
            rank=request.POST["rank"]
            category=request.POST['category']
            branch=request.POST["branch"]

            new_college=College.objects.create(
                college_Name=college_name,
                college_ID=college_id,
                location=location,
                rank=rank,
                category=category,
                branch=branch)
            return redirect('/all_college/')


        return render(request,"create.html")
    else:
        return redirect('/get_rank/')

def all_college(request):
    all_clg=College.objects.all().order_by("rank")
    return render(request,"all_college.html",{"all_clg":all_clg})

def get_rank(request):
    user=request.user
    if request.method=="POST":
        return redirect("/get_list/")

    return render(request,'get_rank.html')

def get_list(request):
    user_rank = request.POST["rank"]
    user_category = request.POST["category"]
    user_branch=request.POST["branch"]
    college_list=College.objects.filter(rank__gte=user_rank, category=user_category,branch=user_branch).order_by("rank")
    return render(request,'get_list.html',{"college_list":college_list})

def edit_college(request,college_id):
    clg=College.objects.get(pk=college_id)

    if request.method=="POST":
        clg_name=request.POST["clg_name"]
        clg_id=request.POST["clg_id"]
        branch=request.POST["branch"]
        rank=request.POST["rank"]
        category=request.POST["category"]
        location=request.POST["location"]
        about=request.POST["about"]
        clg.college_Name=clg_name
        clg.college_ID=clg_id
        clg.branch=branch
        clg.rank=rank
        clg.category=category
        clg.location=location
        clg.about=about
        clg.save()
        return redirect("/all_college/")

    return render(request,"edit_college.html",{"clg":clg})


def delete_college(request,college_id):
    clg=College.objects.get(pk=college_id)
    clg.delete()
    return redirect("/all_college/")
    