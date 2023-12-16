from django.shortcuts import render,get_object_or_404
from .models import ProductModel,Category
from django.http import HttpResponse
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

def category_name(request,id):
    category_id = id
    category = get_object_or_404(Category,id = category_id)
                                            
    product = ProductModel.objects.filter(product_categary =category_id)
    context ={
        'info' : product
    }
    return render(request,'product-category-detail.html',context)