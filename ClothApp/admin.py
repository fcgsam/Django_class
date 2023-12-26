from django.contrib import admin
from .models import Category,ProductModel
from account.models import Account
from django.utils.html  import format_html


class Customproduct(admin.ModelAdmin):
    list_display=['product_name','product_price','gender','product_description','img_display']
    list_filter = ['gender','product_categary']
    list_per_page = 5
    search_fields = ['product_name']

    def img_display(self,obj):
        return format_html("<img src='{}' , width='90' , height='100' />",obj.product_image.url)

# Register your models here.
admin.site.register(Category)
admin.site.register(ProductModel,Customproduct)
admin.site.register(Account)
admin.site.site_header = 'Cloth Store Application'
admin.site.index_title = 'Cloth Store Admin'