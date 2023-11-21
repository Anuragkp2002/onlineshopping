from django.db import models

class register_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    Dateofbirth=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    Phonenumber=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class cart_tb(models.Model):
    Productid=models.ForeignKey("seller.Product_tb",on_delete=models.CASCADE)
    Buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Shippingaddress=models.CharField(max_length=20)
    Quantity=models.CharField(max_length=20)
    Total=models.CharField(max_length=20)
class order_tb(models.Model):
    Customername=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Phonenumber=models.CharField(max_length=20)
    Buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Status=models.CharField(max_length=20,default="pending")
    Orderdate=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Grandtotal=models.IntegerField()
class orderitem_tb(models.Model):
    Orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
    Productid=models.ForeignKey("seller.Product_tb",on_delete=models.CASCADE)
    Buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Total=models.IntegerField()
class payment_tb(models.Model):
    Orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)    
    Buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Cardnumber=models.CharField(max_length=20)
    CardholderName=models.CharField(max_length=20)
    Expirydate=models.CharField(max_length=20)
    CVV=models.CharField(max_length=20)
