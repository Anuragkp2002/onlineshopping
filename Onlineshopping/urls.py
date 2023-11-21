"""
URL configuration for Onlineshopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('loginAction/',views.loginAction,name="loginAction"),
    path('buyerregister/',buyerview.buyerregister,name="buyerregister"),
    path('buyerregisterAction/',buyerview.buyerregisterAction,name="buyerregisterAction"),
    path('sellerregister/',sellerview.sellerregister,name="sellerregister"),
    path('sellerregisterAction/',sellerview.sellerregisterAction,name="sellerregisterAction"),
    path('viewseller/',views.viewseller,name="viewseller"),
    path('approve <int:id>/',views.approve,name="approve"),
    path('reject <int:id>/',views.reject,name="reject"),
    path('editprofile/',sellerview.editprofile,name="editprofile"),
    path('editAction/',sellerview.editAction,name="editAction"),
    path('category/',views.category,name="category"),
    path('categoryAction/',views.categoryAction,name="categoryAction"),
    path('productdetails/',sellerview.productdetails,name="productdetails"),
    path('productdetailsAction/',sellerview.productdetailsAction,name="productdetailsAction"),
    path('productview/',sellerview.productview,name="productview"),
    path('edit <int:id>/',sellerview.edit,name="edit"),
    path('producteditAction/',sellerview.producteditAction,name="producteditAction"),
    path('delete <int:id>/',sellerview.delete,name="delete"),
    path('buyeredit/',buyerview.buyeredit,name="buyeredit"),
    path('buyereditAction/',buyerview.buyereditAction,name="buyereditAction"),
    path('viewproduct/',buyerview.viewproduct,name="viewproduct"),
    path('cart<int:id>/',buyerview.cart,name="cart"),
    path('cartAction/',buyerview.cartAction,name="cartAction"),
    path('cartview/',buyerview.cartview,name="cartview"),
    path('cartviewAction/',buyerview.cartviewAction,name="cartviewAction"),
    path('paynow<int:id>/',buyerview.paynow,name="paynow"),
    path('paynowAction/',buyerview.paynowAction,name="paynowAction"),
    path('orderdetails/',buyerview.orderdetails,name="orderdetails"),
    path('details<int:id>/',buyerview.details,name='details'),
    path('cancel<int:id>/',buyerview.cancel,name='cancel'),
    path('vieworder/',sellerview.vieworder,name='vieworder'),
    path('Details<int:id>',sellerview.Details,name='Details'),
    path('Approve<int:id>/',sellerview.Approve,name="Approve"),
    path('Reject<int:id>/',sellerview.Reject,name="Reject"),
    path('Confirmcancel<int:id>/',sellerview.Confirmcancel,name="Confirmcancel"),
    path('Trackdetails<int:id>/',sellerview.Trackdetails,name="Trackdetails"),
    path('TrackdetailsAction/',sellerview.TrackdetailsAction,name="TrackdetailsAction"),
    path('Trackview<int:id>/',buyerview.Trackview,name="Trackview"),
    path('viewproductAction/',buyerview.viewproductAction,name="viewproductAction"),
    path('home/',buyerview.home,name="home"),
    path('changepassword/',buyerview.changepassword,name="changepassword"),
    path('changepasswordAction/',buyerview.changepasswordAction,name="changepasswordAction"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('forgotpasswordAction/',views.forgotpasswordAction,name="forgotpasswordAction"),
    path('forgotAction/',views.forgotAction,name="forgotAction"),
    path('newpasswordAction/',views.newpasswordAction,name="newpasswordAction"),
    path('existing/',buyerview.existing,name="existing"),
    path('sellerexist/',sellerview.sellerexist,name="sellerexist"),
    path('searchAction/',sellerview.searchAction,name="searchAction"),
    path('sellerpshome/',sellerview.sellerpshome,name="sellerpshome"),
    path('Changepassword/',sellerview.Changepassword,name="Changepassword"),
    path('ChangepasswordAction/',sellerview.ChangepasswordAction,name="ChangepasswordAction"),
    path('logout/',sellerview.logout,name="logout"),
    path('logout/',buyerview.logout,name="logout")

    

 
    

    

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

