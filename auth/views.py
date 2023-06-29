from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"auth/index.html")

def signup(request): 
    if request.method == "POST":
        user_name = request.POST["user_name"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        myuser = User.objects.create_user(user_name,email,password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request,"Account successfully created.")
        return redirect("signin")

    return render(request,"auth/signup.html")

def signin(request):
    # if request.method == "POST":
    #     user_name = request.POST["user_name"]
    #     pass1 = request.POST["password"]

    #     user =  authenticate(username = user_name, password = pass1)
    #     if user is not None:
    #         login(request,user)
    #         first_name = user.first_name
    #         return redirect(request,"auth/index.html",{"first_name" : first_name})
    #     else:
    #         messages.error(request, "bad credintial")
    #         return redirect("home")

    return render(request,"auth/signin.html")

def signout(request):
    pass   