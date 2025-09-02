from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import login as user_login, logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
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
        
        if user is None:
            raise ValidationError("Invalid username and password")
        print(username, password)
        if user is not None:
            user_login(request, user)
            return redirect('home')  
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

@login_required
def home(request):
    return render(request,'home.html')


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def reset_pass(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        user= User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request,'reset-password.html')




def change_pass(request):
    if request.method =="POST":
        user =request.user
        old_password= request.POST.get('old_password')
        new_password= request.POST.get('new_password')
        confirm_new_password= request.POST.get('confirm_password')

        if not user.check_password(old_password):
            messages.error(request, "Old password is incorrect.")
            return redirect('change_password')
        
        if new_password != confirm_new_password:
            messages.error(request, "New password and confirm password do not match.")
            return redirect('change_password')
        
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  
        
        return redirect('home')
    return render(request, 'change-password.html')        


def forgot_pass(request):
    if request.method=="POST":
        username= request.POST.get('username')
        new_password=request.POST.get('new_password')
        confirm_new_password=request.POST.get('confirm_password')

        if new_password != confirm_new_password:
            raise ValidationError("Passwords do not match")
        
        user= User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return redirect('login')
    return render(request,'forgot-password.html')