from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import TreeForeignKey

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', default='user.png')
    STATUS=(
        ('user','user'),
        ('Admin','Admin')
        )
    status=models.CharField(choices=STATUS,max_length=70,default='user')


class Category(models.Model):
    name=models.CharField(max_length=500)
    parent=TreeForeignKey('self',verbose_name='ichki_tur',on_delete=models.CASCADE)
    rasm=models.ImageField(upload_to='category_img/')


class Product(models.Model):
    name=models.CharField(max_length=1000)
    batafsil=models.TextField()
    price=models.CharField(max_length=700)
    category=models.ForeignKey(Category,verbose_name='productlar',on_delete=models.CASCADE)
    user=models.ForeignKey(User,verbose_name='productlar',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


class Product_imgs(models.Model):
    rasm=models.ImageField(upload_to='product_imgs/')
    product=models.ForeignKey(Product,verbose_name='rasmlar',on_delete=models.CASCADE)
