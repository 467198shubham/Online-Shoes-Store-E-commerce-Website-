from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    cname=models.CharField(max_length=120)
    
    def __str__(self):
        return self.cname
    
    class meta:
        db_table="Category"
#class Shoe(models.Model):          
class Shoes(models.Model):
    #shoename=models.CharField(max_length=120)
    shoesName=models.CharField(max_length=120)
    price=models.FloatField(default=100)
    description=models.CharField(max_length=120)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    imageurl=models.ImageField(upload_to=settings.MEDIA_ROOT)
    
    class meta:
        db_table="Shoes"
class contact(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    country=models.CharField(max_length=120)
    subject=models.CharField(max_length=500)
    
    class meta:
        db_table='contact'
        
class UserInfo(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    
    class meta:
        db_table="UserInfo"

class MyCart(models.Model):
    username =models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    #shoe=models.ForeignKey(Cake,on_delete=models.CASCADE)
    shoes=models.ForeignKey(Shoes,on_delete=models.CASCADE)
    qty=models.FloatField(default=10)
    
    class meta:
        db_table="MyCart"
        
class CardDetails(models.Model):
    cardno = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    expiry= models.CharField(max_length=4)
    amount=models.FloatField(default=10000)
    
    class Meta:
        db_table="CardDetails"