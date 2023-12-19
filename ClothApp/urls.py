from django.urls import path
from . import views              #from views import home_page

urlpatterns = [
    path('',views.home_page,name='home'),
    path('product-detail/<int:id>/',views.productDetails,name='product-detail'),
    path('category_name/<int:id>',views.category_name,name='category_name'),
    path('search/',views.search_product,name='search'),
]