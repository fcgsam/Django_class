from django.db import models
from ClothApp.models import ProductModel
from account.models import Account
# Create your models here.
class CartItem(models.model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete = models.CASCADE)
    quentity = models.PositiveIntegerField(default =1)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.quentity} X {self.product.product_name}"
class Cart(models.model):
    user = models.OneToOneField(Account,on_delete =models.CASCADE)
    items = models.ManyToManyField(CartItem)
    creted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Cart for {self.user.email}"