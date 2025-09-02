from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import login as user_login, logout as user_logout, authenticate 
# Create your views here.

def register_view(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST) #receive data form user request
        if form.is_valid():
            password= form.cleaned_data["password"]
            confirm_password=form.cleaned_data['confirm_password']

            if password != confirm_password: # Check password and confirm password, is matched ?
                raise ValidationError("Passwords do not match")

            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect('login') # redirect in log in after save user data 
    form=UserRegisterForm()
    return render(request,'index_register.html',{'form':form})

"""
In this view we use Form for peek data and for validation.. 
if we don't use form then we get data 

    ```
    def register_view(request):
        if request.method=="POST":
            username=request.POST.get('username')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            
            if username and password not None:
                if password != confirm_password: # Check password and confirm password, is matched ?
                    raise ValidationError("Passwords do not match")
                user= User.object.create_user(
                    username=username,
                    first_name=first_name, 
                    last_name=last_name,  
                    email=email,  
                    password=password,  
                    ) 
                return redirect('login')
        return render(request,'index_register.html')
    ```
    in template we should add specific name in input field.
    <input type="text" id="lastName" name="lastName" placeholder="Last name" required>
"""


def login_view_username_pass(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('register')  
    return render(request,'login.html')

"""
without Form get data using request.POST.get('....')
if we use form for login

``` 
    def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")  
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})
"""