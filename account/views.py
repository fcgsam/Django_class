from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def registration_form(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request,'register_form.html',{'form_data':form})
    if request.method == 'POST':
        pass
    form = RegistrationForm()
    return render(request,'register_form.html',{'form_data':form})
    
    