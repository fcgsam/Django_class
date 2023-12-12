from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=100)


    # This part return th value not object
    def __str__(self):
        return self.Category_name

class ProductModel(models.Model):
    gender_option =(('M','Male',),('F','female'),('B','Both'))
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='product_image',default=None)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_categary = models.ForeignKey(Category,on_delete=models.CASCADE)
    gender = models.CharField(max_length=30,choices=gender_option)

    # if u want to give column name by ur own
    class Meta:
        db_table = "product"
    def __str__(self):
        return self.product_name