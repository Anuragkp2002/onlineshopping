from django.shortcuts import render,redirect
from django.contrib import messages
from seller.models import *
from siteadmin.models import *
from buyer.models import *
import datetime
from django.http import JsonResponse


# Create your views here.
def sellerregister(request):
    return render(request,'sellerregister.html')
def sellerregisterAction(request):
    Name=request.POST["name"]
    Gender=request.POST["gender"]
    DOB=request.POST["dob"]    
    Phonenumber=request.POST["Phonenumber"]
    Country=request.POST["country"]
    if len(request.FILES)>0:
        File=request.FILES['file']
    else:
        File="no pic"
    File=request.FILES["file"]
    Username=request.POST["username"]
    Password=request.POST["password"]
    seller=sellerregister_tb(Name=Name,Gender=Gender,DOB=DOB,Phonenumber=Phonenumber,Country=Country,File=File,Username=Username,Password=Password)
    seller.save()
    messages.add_message(request,messages.INFO,'Registration Succesfull')
    return redirect('sellerregister')
def editprofile(request):
    e=sellerregister_tb.objects.filter(id=request.session["sellerid"])
    return render(request,"editprofile.html",{'ed':e})   
def editAction(request):
    id=request.session["sellerid"]
    seller=sellerregister_tb.objects.filter(id=id)
    if len(request.FILES)>0:
        img=request.FILES["File"]
    else:
        img=seller[0].File    
    Name=request.POST["name"]
    Gender=request.POST["gender"]
    DOB=request.POST["dob"]    
    Phonenumber=request.POST["Phonenumber"]
    Country=request.POST["Country"]
    Username=request.POST["Username"]
    Password=request.POST["Password"]
    slr=sellerregister_tb.objects.filter(id=id).update(Name=Name,Gender=Gender,DOB=DOB,Phonenumber=Phonenumber,Username=Username,Password=Password)
    imgupload=sellerregister_tb.objects.get(id=id)
    imgupload.File=img
    imgupload.save()
    return redirect('editprofile')
def productdetails(request):
    category=category_tb.objects.all()
    return render(request,'productdetails.html',{'ca':category})    
def productdetailsAction(request):
    id=request.session["sellerid"]
    seller=sellerregister_tb.objects.filter(id=id)
    Name=request.POST["name"]
    if len(request.FILES)>0:
        File=request.FILES['file']
    else:
        File="no pic"
    File=request.FILES["file"]    
    Price=request.POST["price"]    
    Stock=request.POST["stock"]
    Details=request.POST["details"]
    Category=request.POST["category"]
    Product=Product_tb(Name=Name,File=File,Price=Price,Stock=Stock,Details=Details,Categoryid_id=Category,Sellerid_id=id)
    Product.save()
    messages.add_message(request,messages.INFO,'Product Added')
    return redirect('productdetails')
def productview(request):
    id=request.session["sellerid"]
    product=Product_tb.objects.filter(Sellerid=id)    
    return render(request,'productview.html',{'pr':product})
def edit(request,id):
    pro=Product_tb.objects.filter(id=id)
    category=category_tb.objects.all()
    return render(request,'productedit.html',{'pr':pro,'ca':category})
def producteditAction(request):
    sellerid=request.session["sellerid"]
    id=request.POST["id"]
    seller=Product_tb.objects.filter(id=id)
    Name=request.POST["name"]
    if len(request.FILES)>0:
        File=request.FILES['file']
    else:
        File="no pic"
    Price=request.POST["price"]    
    Stock=request.POST["stock"]
    Details=request.POST["details"]
    Category=request.POST["category"]
    productact=Product_tb.objects.filter(id=id).update(Name=Name,File=File,Price=Price,Stock=Stock,Details=Details,Categoryid_id=Category,Sellerid_id=sellerid)
    imgupload=Product_tb.objects.get(id=id)
    imgupload.File=File
    imgupload.save()
    return redirect('productview')
def delete(request,id) :
    prod=Product_tb.objects.filter(id=id).delete() 
    return redirect('productview')
def vieworder(request):
    prdct=Product_tb.objects.filter(Sellerid=request.session["sellerid"])    
    odr=orderitem_tb.objects.filter(Productid__in=prdct)
    ode=order_tb.objects.filter(id__in=odr)
    return render(request,'vieworder.html',{'od':ode})
def Details(request,id):
    prdct=Product_tb.objects.filter(Sellerid=request.session["sellerid"])
    odr=orderitem_tb.objects.filter(Productid__in=prdct,Orderid=id)
    oder=order_tb.objects.filter(id=id)
    return render(request,'sellerorderdetails.html',{'odd':oder,'dr':odr})
def Approve(request,id):
    apr=order_tb.objects.filter(id=id).update(Status='approved')
    return redirect('vieworder')    
def Reject(request,id):
    rj=order_tb.objects.filter(id=id).update(Status='rejected')
    return redirect('vieworder')    
def Confirmcancel(request,id):
    cf=orderitem_tb.objects.filter(Orderid=id)  
    for v in cf:
        pd=Product_tb.objects.filter(id=v.Productid_id)
        qt=v.Quantity
        st=pd[0].Stock
        newstock=qt+st
        update=Product_tb.objects.filter(id=v.Productid_id).update(Stock=newstock)
    Or=order_tb.objects.filter(id=id).update(Status='canceled')
    return redirect('vieworder')  
def Trackdetails(request,id):
    trck=order_tb.objects.filter(id=id)
    return render(request,'track.html',{'tr':trck})   
def TrackdetailsAction(request):
    Details=request.POST["details"]
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:")
    id=request.POST["orderid"]
    orderid=order_tb.objects.get(id=id)
    track=tracking_tb(Details=Details,Date=Date,Time=Time,orderid=orderid)
    track.save()
    return redirect('vieworder')


def sellerexist(request):
    User=request.GET['user']
    seller=sellerregister_tb.objects.filter(Username=User)
    if seller.count()>0:
        msg="exist"
    else:
        msg=" Not exist"
    return JsonResponse({'valid':msg})
def searchAction(request):
    Name=request.POST["name"]
    srch=Product_tb.objects.filter(Name__istartswith=Name ) | Product_tb.objects.filter(Price=Name)
    return render(request,'productview.html',{'pr':srch})  
def sellerpshome(request):
    return render(request,'sellerhome.html')
def Changepassword(request):
    return render(request,'sellerpassword.html')     
def ChangepasswordAction(request):
    id=request.session["sellerid"]   
    Currentpassword=request.POST["currentpassword"]
    Newpassword=request.POST["newpassword"]
    Retypenewpassword=request.POST["retypenewpassword"]
    Seller=sellerregister_tb.objects.filter(id=id,Password=Currentpassword)
    if Seller.count()>0:
        if (Newpassword==Retypenewpassword):
            pas=sellerregister_tb.objects.filter(id=id).update(Password=Newpassword)
            messages.add_message(request,messages.INFO,'Password changed')
        else:                
            messages.add_message(request,messages.INFO,'Incorrect Password')
    else:
        messages.add_message(request,messages.INFO,'Incorrect Password')
    return redirect('sellerpshome')  

def logout(request):
    request.session.flush()
    return redirect('index')











      


