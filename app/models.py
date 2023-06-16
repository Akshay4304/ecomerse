from django.urls import reverse
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,username=None,password=None,*args,**kwargs):
        if username is None:
            raise TypeError('username must not be None')
        if password is None:
            raise TypeError('password must not be None')
        user = self.model(username=username,*args,**kwargs)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
    
    def create_superuser(self,username,password,email):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            role=1,
            is_staff=True,
            )
        user.is_superuser = True
        user.save()
        return user



ROLE_CHOICES = [
    (1,'admin'),
    (2,'customers')
    ]
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=30,unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    objects = UserManager()

    def __str__(self):
        return self.username
    




class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug =models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=300,blank=True)
    cat_image = models.ImageField(upload_to='photos/category',blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
# get url from category 
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    product_discription =models.TextField(max_length=500,blank=True)
    price =models.IntegerField()
    images =models.ImageField(upload_to='photos/product')
    stock = models.IntegerField()
    is_available =models.BooleanField(default=True)
    category =models.ForeignKey(Category,on_delete=models.CASCADE) 
    created_date = models.DateTimeField(auto_now_add =True)
    modified_date =models.DateTimeField(auto_now =True)
    

    def get_url(self):
        return reverse('product_details',args=[self.category.id,self.id])

    def __str__(self):
        return self.product_name
    

