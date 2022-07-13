from django.shortcuts import render,redirect
from site_seller.models import *
from site_buyer.models import *
from site_admin.models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime
# Create your views here.
def buyerregister(request):
    return render(request,'buyerregister.html')
def buyerregisterAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    phone=request.POST['phone']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    user=buyer_tb(name=name,dob=dob,gender=gender,country=country,phone=phone,address=address,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"registration successfull")
    return redirect('buyerregister')
def viewuserProduct(request):
    product=product_tb.objects.all()
    return render(request,'viewuserProduct.html',{'data':product})
def addtocart(request,uid):
    buyer=product_tb.objects.filter(id=uid)
    return render(request,'addtocart.html',{'data':buyer})
def addtocartAction(request):
    productid=request.POST['productid']
    productid_obj=product_tb.objects.get(id=productid)
    buyerid=request.session['id']
    buyerid_obj=buyer_tb.objects.get(id=buyerid)
    shippingadress=request.POST['shippingadress']
    contactno=request.POST['contactno']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    stock=productid_obj.stock
    if(int(quantity)>stock):
        messages.add_message(request,messages.INFO,"required quantity not available")
    else:
     buyer=cart_tb(productid=productid_obj,buyerid=buyerid_obj,shippingadress=shippingadress,contactno=contactno,quantity=quantity,totalprice=totalprice)
     buyer.save()
     messages.add_message(request,messages.INFO,"product added to cart")
    return redirect('addtocart',uid=productid)
def viewcart(request):
    buyerid=request.session['id']
    cart=cart_tb.objects.filter(buyerid=buyerid)
    return render(request,'viewcart.html',{'data':cart})
def deletecart(request,uid):
    buyer=cart_tb.objects.filter(id=uid).delete()
    return redirect('viewcart')
def placeorderAction(request):
    cart_items=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    for cid in cart_items:
        item=cart_tb.objects.filter(id=cid)
        productid=item[0].productid
        buyerid=item[0].buyerid
        sellerid=item[0].productid.sellerid
        shippingaddress=item[0].shippingadress
        quantity=item[0].quantity
        totalprice=item[0].totalprice
        stock=item[0].productid.stock
        if(int(quantity)>stock):
            messages.add_message(request,messages.INFO,"required quantity not available")
        else:
            buyer=order_tb(productid=productid,buyerid=buyerid,sellerid=sellerid,shippingaddress=shippingaddress,quantity=quantity,totalprice=totalprice,date=date,time=time)
            buyer.save()
            stocknew=stock-quantity
            product=product_tb.objects.filter(id=productid.id)
            product.update(stock=stocknew)
            item.delete()
            messages.add_message(request,messages.INFO,"ordered successfully")
        return redirect('viewcart')
def viewOrders(request):
    buyerid=request.session['id']
    order=order_tb.objects.filter(buyerid=buyerid)
    return render(request,'viewOrders.html',{'data':order})
def cancel(request,uid):
    product=order_tb.objects.filter(id=uid)
    product.update(status='Cancellation successfull')
    product1=product[0].productid
    productid=product1.id
    quantity=product[0].quantity
    productid_obj=product_tb.objects.filter(id=productid)
    stock=productid_obj[0].stock
    stocknew=stock+quantity
    productid_obj.update(stock=stocknew)
    return redirect('viewOrders')
def viewtrackingDetails(request,uid):
    buyer=tracking_tb.objects.filter(orderid=uid).order_by('-id')
    return render(request,'viewtrackingDetails.html',{'data':buyer})
def searchProduct(request):
    return render(request,'searchProduct.html')
def searchProductAction(request):
    search=request.POST['search']
    product=product_tb.objects.filter(productname__istartswith=search)
    return render(request,'viewuserProduct.html',{'data':product})
def searchproductbycategoryandprice(request):
    category=category_tb.objects.all()
    return render(request,'searchproductbycategoryandprice.html',{'data':category})
def searchproductbycategoryandpriceAction(request):
    category=request.POST['category']
    price=request.POST['price']
    product=product_tb.objects.filter(category=category,price__lte=price)
    return render(request,'viewuserProduct.html',{'data':product})
def updateProfile(request):
    buyerid=request.session['id']
    buyer=buyer_tb.objects.filter(id=buyerid)
    return render(request,'updateProfile.html',{'data':buyer})
def updateProfileAction(request):
    buyerid=request.session['id']
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    phone=request.POST['phone']
    address=request.POST['address']
    username=request.POST['username']
    buyer=buyer_tb.objects.filter(id=buyerid).update(name=name,dob=dob,gender=gender,country=country,phone=phone,address=address,username=username)
    messages.add_message(request,messages.INFO,"updated profile")
    return redirect('updateProfile')
                        

    

           
    

