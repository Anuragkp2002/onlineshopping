from django.shortcuts import render,redirect
from django.contrib import messages
from siteadmin.models import *
from buyer.models import *
from seller.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')    
def loginAction(request):  
    Username=request.POST['username']
    Password=request.POST['password']    
    admin=admin_tb.objects.filter(username=Username,password=Password)
    buyer=register_tb.objects.filter(Username=Username,Password=Password)
    seller=sellerregister_tb.objects.filter(Username=Username,Password=Password)
    if admin.count()>0:
        request.session['id']=admin[0].id       
        return render(request,'home.html')
    elif buyer.count()>0:
        request.session['buyerid']=buyer[0].id
        return render(request,'buyerhome.html') 
    elif seller.count()>0:
        if seller[0].Status=="approved":
            request.session['sellerid']=seller[0].id
            return render(request,'sellerhome.html')
        else:
             messages.add_message(request,messages.INFO,'User not found')
             return redirect('index')
    else:
        messages.add_message(request,messages.INFO,'Login failed')
        return redirect('index')
def viewseller(request):
    seller=sellerregister_tb.objects.all()
    return render(request,'viewseller.html',{'se':seller})   
def approve(request,id):
    ap=sellerregister_tb.objects.filter(id=id).update(Status='approved')
    return redirect('viewseller')
def reject(request,id):
    re=sellerregister_tb.objects.filter(id=id).update(Status='rejected')
    return redirect('viewseller')  
def category(request):
    return render(request,'category.html')   
def categoryAction(request):
    Name=request.POST["Name"] 
    category=category_tb(categoryname=Name)  
    category.save()
    return redirect('category')   
def forgotpassword(request):
    return render(request,'frgtpassword.html')   
def forgotpasswordAction(request):
    Username=request.POST["username"]   
    byr=register_tb.objects.filter(Username=Username)
    slr=sellerregister_tb.objects.filter(Username=Username)
    if byr.count()>0:
        return render(request,'forgot.html',{'ad':Username})
    elif slr.count()>0:
        return render(request,'forgot.html',{'ad':Username}) 
    else:
        messages.add_message(request,messages.INFO,'Incorrect Username')
        return redirect('index')  
def forgotAction(request):
    Username=request.POST["username"]
    Name=request.POST["name"] 
    Phonenumber=request.POST["phonenumber"] 
    Country=request.POST["country"]   
    br=register_tb.objects.filter(Name=Name,Phonenumber=Phonenumber,Country=Country)   
    sr=sellerregister_tb.objects.filter(Username=Username,Name=Name,Phonenumber=Phonenumber,Country=Country)     
    if br.count()>0:
        return render(request,'newpassword.html',{'sr':Username})
    elif sr.count()>0:
        return render(request,'newpassword.html',{'sr':Username})   
    else:
        messages.add_message(request,messages.INFO,'Incorrect details')    
        return redirect('index') 
def newpasswordAction(request):
    Username=request.POST["username"]
    Newpassword=request.POST["newpassword"]
    Retypenewpassword=request.POST["retypenewpassword"]
    if (Newpassword == Retypenewpassword):
        buyer=register_tb.objects.filter(Username=Username)
        seller=sellerregister_tb.objects.filter(Username=Username)
        if buyer.count()>0:
            id=buyer[0].id
            ps=register_tb.objects.filter(id=id).update(Password=Newpassword)
            messages.add_message(request,messages.INFO,'Password changed')
            return redirect('index') 
        elif  seller.count()>0:
            sellerid=seller[0].id    
            paws=sellerregister_tb.objects.filter(id=sellerid).update(Password=Newpassword)
            messages.add_message(request,messages.INFO,'Password changed')
            return redirect('index') 
        else:    
            messages.add_message(request,messages.INFO,' Incorrect username')
            return redirect('index')
    else:
        messages.add_message(request,messages.INFO,'Check your password')
        return redirect('index') 
    
        
    
         
