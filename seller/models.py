from django.db import models

# Create your models here.
class sellerregister_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    Phonenumber=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    File=models.FileField()
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Status=models.CharField(max_length=20,default='pending')
class Product_tb(models.Model):
    Name=models.CharField(max_length=20)
    File=models.FileField()
    Price=models.CharField(max_length=20) 
    Stock=models.IntegerField()
    Details=models.CharField(max_length=20)
    Sellerid=models.ForeignKey(sellerregister_tb,on_delete=models.CASCADE)   
    Categoryid=models.ForeignKey("siteadmin.category_tb",on_delete=models.CASCADE)   
class tracking_tb(models.Model):
    orderid=models.ForeignKey("buyer.order_tb",on_delete=models.CASCADE)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Details=models.CharField(max_length=20)    

