from django.shortcuts import render
from .forms import RegistrationForm,UserLoginForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import Account
from django.contrib.auth.decorators import  login_required


# Create your views here.
def registration_form(request):
    form = RegistrationForm()
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully.')
            return redirect('home')
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    messages.error(request,f'{field.capitalize()}:{error}')
            return render(request,'register_form.html',{'form_data':form})

    return render(request,'register_form.html',{'form_data':form})

def login_form(request):
    if request.method=="POST":
        try:
            email = request.POST['email']
            password =request.POST['password']
            user =Account.objects.get(email=email)
            result = Account.objects.filter(email__icontains = user).values()

            if user.check_password(password):
                
                login(request,user,backend='account.backends.MyBackEnd')

                messages.success(request,f'Wellcome {result[0]['username']} You have logged in Successfully.')
                return redirect('home')
            else:
                messages.error(request,'Account not found or Incorrect Credentials')
        except:
            pass
    return render(request,'login.html')

@login_required(login_url='login')
def user_logout(request):

    logout(request)
    messages.success(request,'You have Logged Out')
    return redirect('home')