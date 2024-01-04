from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import redirect

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
    
    