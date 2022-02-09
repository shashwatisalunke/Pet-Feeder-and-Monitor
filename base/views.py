from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import MyUser, Pet
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def ourProduct(request):
    return render(request, 'base/our-product.html')

def aboutUs(request):
    return render(request, 'base/about-us.html')

@login_required(login_url='login')
def scheduler(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q == "add-pet": return redirect('add-pet')
    context = {
        "pet":q,
    }
    return render(request, 'base/scheduler.html', context)

@login_required(login_url='login')
def status(request):
    q = request.GET.get('q') if request.GET.get('q') != None else None
    if q == "add-pet": return redirect('add-pet')
    context = {
        "pet":q,
    }
    return render(request, 'base/status.html', context)
    
@login_required(login_url='login')
def addPet(request):
    return render(request, 'base/add-pet.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        send_mail(
            "There ia query from your website", 
            f"Hi! {name} here, {message}. contact me on Email-{email}, Ph-{number}", 
            settings.EMAIL_HOST_USER, 
            ["email@email.com"], 
            False
        )
    return render(request, 'base/contact-us.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        if request.POST.get('signIn'):
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')
            try:
                username = MyUser.objects.get(email=email).username
            except:
                messages.info(request, "User does not exist")
                return redirect('login')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Invalid Credintials")
                return redirect('login')

        elif request.POST.get('signUp'):
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if MyUser.objects.filter(email=email).exists():
                    messages.error(request, "Email already Used")
                    return redirect('login')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, "Username already Used")
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    myuser = MyUser.objects.create(
                            user=user, 
                            name=name, 
                            email=email,
                            username=username,
                        )
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, "Password does not match")
                return redirect('login')
        else:
            messages.error(request, "An error occured during registraion")
            return redirect('login')

    return render(request, 'base/login.html')

def userLogout(request):
    logout(request)
    return redirect('home')

def resetPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = MyUser.objects.get(email=email).user
            except:
                messages.info(request, "User does not exist")
                return redirect('reset-password')
            if user is not None:
                user.set_password(password1)
                user.save()
                messages.info(request, "Password Reset Successful")
                return redirect('login')
            else:
                messages.info(request, "An error occured during password reset")
        else:
            messages.info(request, "Password does not match")
            return redirect('reset-password')
    return render(request, 'base/reset-password.html')