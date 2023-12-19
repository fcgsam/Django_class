from django.shortcuts import render,get_object_or_404
from .models import ProductModel,Category
from django.http import HttpResponse,Http404
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

def search_product(request):
    if request.method == 'GET':
        search_data = request.GET.get('search')
        if(len(search_data)==0):
            raise Http404('please provide valid data')
        else:
            # for description too first import from django.db.models import Q
            # result = ProductModel.objects.filter(Q(product_name__icontains = search_data) | Q(product_description__icontains = search_data))
            result = ProductModel.objects.filter(product_name__icontains = search_data)
            context = {
                'info':result
            }

            return render(request,'search.html',context)