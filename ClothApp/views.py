from django.shortcuts import render
from .models import ProductModel

# Create your views here.
def home_page(request):
    all_data = ProductModel.objects.all()
    context = {
        'info': all_data
    }
    return render(request,'index.html',context)

def productDetails(request,id):
    get_data = ProductModel.objects.get(id=id)
    context ={
        'get_info' : get_data
    }
    return render(request,'product_detail.html',context)