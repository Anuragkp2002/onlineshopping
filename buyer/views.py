from django.shortcuts import render,redirect
from django.contrib import messages
from buyer.models import *
from seller.models import *
import datetime
from django.http import JsonResponse



def buyerregister(request):
    return render(request,'buyerregister.html')
def buyerregisterAction(request):
    Name=request.POST["name"]
    Gender=request.POST["gender"]
    Age=request.POST["age"]
    Dateofbirth=request.POST["dateofbirth"]
    Country=request.POST["country"]
    Phonenumber=request.POST["phonenumber"]
    Username=request.POST["username"]
    Password=request.POST["password"]
    buyer=register_tb(Name=Name,Gender=Gender,Age=Age,Dateofbirth=Dateofbirth,Country=Country,Phonenumber=Phonenumber,Username=Username,Password=Password)
    buyer.save()
    messages.add_message(request,messages.INFO,'Registration Succesfull')
    return redirect('buyerregister')
def buyeredit(request):
    e=register_tb.objects.filter(id=request.session["buyerid"])
    return render(request,"buyeredit.html",{'edi':e})
def buyereditAction(request):
    id=request.session["buyerid"]
    Name=request.POST["name"]
    Gender=request.POST["gender"]
    Age=request.POST["age"]
    Dateofbirth=request.POST["dateofbirth"]
    Country=request.POST["country"]
    Phonenumber=request.POST["phonenumber"]
    Username=request.POST["username"]
    Password=request.POST["password"]
    buy=register_tb.objects.filter(id=id).update(Name=Name,Gender=Gender,Age=Age,Dateofbirth=Dateofbirth,Country=Country,Phonenumber=Phonenumber,Username=Username,Password=Password)
    messages.add_message(request,messages.INFO,'Updated Succesfully')
    return redirect('buyeredit')
def viewproduct(request):
    pdct=Product_tb.objects.all()
    return render(request,"viewproduct.html",{'pd':pdct})
def cart(request,id):
    pd=Product_tb.objects.filter(id=id)
    return render(request,"cart.html",{'pc':pd})  
def cartAction(request):
    id=request.session["buyerid"]
    Shippingaddress=request.POST["shippingAddress"]
    Stock=request.POST["stock"]
    Productid=request.POST["id"]
    Quantity=request.POST["quantity"]
    Total=request.POST["total"]
    if int(Stock)>int(Quantity):
        cart=cart_tb(Shippingaddress=Shippingaddress,Productid_id=Productid,Quantity=Quantity,Total=Total,Buyerid_id=id)
        cart.save()
        messages.add_message(request,messages.INFO,'Added to Cart')
    else:
        messages.add_message(request,messages.INFO,'Out of stock')
    return redirect('viewproduct')
def cartview(request):
    id=request.session["buyerid"]
    crt=cart_tb.objects.filter(Buyerid=id)
    return render(request,"cartview.html",{'ct':crt})    
def cartviewAction(request):
    id=request.session["buyerid"]
    Grandtotal=request.POST["grandtotal"]
    CustomerName=request.POST["customername"] 
    Address=request.POST["address"]
    Orderdate=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:")
    Phonenumber=request.POST["phonenumber"]  
    cart=request.POST.getlist('checkbox')
    if len(cart)!=0:
        odr=order_tb(Grandtotal=Grandtotal,Customername=CustomerName,Address=Address,Orderdate=Orderdate,Time=Time,Phonenumber=Phonenumber,Buyerid_id=id)
        odr.save()
        for cid in cart:
            item=cart_tb.objects.filter(id=cid)
            quantity=item[0].Quantity
            Productid=item[0].Productid
            Total=item[0].Total
            Stock=item[0].Productid.Stock
            Newstock=int(Stock)-int(quantity)
            cart=Product_tb.objects.filter(id=Productid.id).update(Stock=Newstock)
            prdct=orderitem_tb(Orderid_id=odr.id,Quantity=quantity,Productid=Productid,Total=Total,Buyerid_id=id)
            prdct.save() 
        return redirect('paynow',odr.id)      
        messages.add_message(request,messages.INFO,'product ordered')
    else:
        messages.add_message(request,messages.INFO,'order failed')
    return redirect('viewproduct')
def paynow(request,id):
    ptd=order_tb.objects.filter(id=id)
    return render(request,'paynow.html',{'pd':ptd})
def paynowAction(request):
    id=request.session["buyerid"]    
    Cardnumber=request.POST["Cardnumber"]
    CardholderName=request.POST["cardholdername"]
    Expirydate=request.POST["expirydate"]
    CVV=request.POST["cvv"]
    Orderid=request.POST["orderid"]
    pay=payment_tb(Orderid_id=Orderid,Cardnumber=Cardnumber,CardholderName=CardholderName,Expirydate=Expirydate,CVV=CVV,Buyerid_id=id)
    pay.save()
    messages.add_message(request,messages.INFO,'Payment Succesfull')
    return redirect('viewproduct')

def orderdetails(request):
    id=request.session["buyerid"]
    det=order_tb.objects.filter(Buyerid_id=id)
    return render(request,'orderdetails.html',{'dt':det})    
def details(request,id):
    orderdetails=orderitem_tb.objects.filter(Orderid=id,Buyerid=request.session["buyerid"]).select_related('Orderid')
    det=order_tb.objects.filter(id=id)
    return render(request,'details.html',{'de':det,'od':orderdetails})
def cancel(request,id):
    can=order_tb.objects.filter(id=id).update(Status='canceled')    
    return redirect('viewproduct')
def Trackview(request,id):
    tck=tracking_tb.objects.filter(orderid=id)  
    if len(tck)>0:
        return render(request,'trackview.html',{'tk':tck}) 
    else:
        messages.add_message(request,messages.INFO,'No Data to Show')
    return redirect('orderdetails')
def viewproductAction(request):
    Name=request.POST["productname"]
    srch=Product_tb.objects.filter(Name__istartswith=Name ) | Product_tb.objects.filter(Price=Name)
    return render(request,'viewproduct.html',{'pd':srch})
def home(request):
    return render(request,'buyerhome.html')    
def changepassword(request):
    return render(request,'password.html')
def changepasswordAction(request):
    id=request.session["buyerid"]    
    Currentpassword=request.POST["currentpassword"]
    Newpassword=request.POST["newpassword"]
    Confirmpassword=request.POST["confirmpassword"]
    Buyer=register_tb.objects.filter(id=id,Password=Currentpassword)
    if Buyer.count()>0:
        if (Newpassword==Confirmpassword):
            pas=register_tb.objects.filter(id=id).update(Password=Newpassword)
            messages.add_message(request,messages.INFO,'Password changed')
        else:
            messages.add_message(request,messages.INFO,'Incorrect password')
    else:
        messages.add_message(request,messages.INFO,'Incorrect password')
    return redirect('home')    

def existing(request):
    Username=request.GET['user']
    user=register_tb.objects.filter(Username=Username)
    if user.count()>0:
        msg="exist"
    else:
        msg=" Not exist"
    return JsonResponse({'valid':msg})

def logout(request):
    request.session.flush()
    return redirect('index')

     


