from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def craete_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email Address')
        if not username:
            raise ValueError("User must have an user name")

        user = self.model(
            email = self.normalize_email(email)
            username = username
            password = password
            first_name = first_name
            last_name= last_name
        )
            
            
        def Create_superuser(self,first_name,last_name,email,username,password):
            user = self.craete_user(
                email = self.normalize_email(email)
                username = username
                password = password
                first_name = first_name
                last_name= last_name

            )
                
            
            user.is_admin = True
            user.is_active = True
            user.is_staff = True
            user.is_superadmin = True
            user.save(using = self.db)
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=100,unique = True)
    email=models.EmailField(max_length = 100,unique = True)
    phone_number =models.CharField(max_length=10)

    #not reqired
    date_joined  = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now_add = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username','first_name','last_name']
    def __str__(self):
        return self.email


    def has_perm(self,perm,obj = None):
        return self.is_admin
    def has_model_perm(self,add_label):
        return True
    
        
        