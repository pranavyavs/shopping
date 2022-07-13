from django.shortcuts import render,redirect 
from site_seller.models import *
from site_buyer.models import*
from site_admin.models import*
from django.contrib import messages
from django.http import JsonResponse
import datetime
# Create your views here.
def sellerregister(request):
    return render(request,'sellerregister.html')
def sellerregisterAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    phone=request.POST['phone']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    if len(request.FILES)>0:
        image=request.FILES['proofupload']
    else:
        image="no pic"
    user=sellerregister_tb(name=name,dob=dob,gender=gender,country=country,phone=phone,address=address,username=username,password=password,proofupload=image)
    user.save()
    messages.add_message(request,messages.INFO,"registration successfull")
    return redirect('sellerregister')
def checkUsername(request):
    username=request.GET['username']
    print(username)
    seller=sellerregister_tb.objects.filter(username=username)
    buyer=buyer_tb.objects.filter(username=username)
    if len(seller)>0:
        msg="exists"
   
    elif len(buyer)>0:
        msg="exists"
    
    else:
        msg="not exists"
    print(msg)
    return JsonResponse({'valid':msg})
def addproduct(request):
    category=category_tb.objects.all()
    return render(request,'addproduct.html',{'category':category})
def addproductAction(request):
    productname=request.POST['productname']
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image="no pic"
    price=request.POST['price']
    details=request.POST['details']
    stock=request.POST['stock']
    category=request.POST['category']
    category_obj=category_tb.objects.get(id=category)
    sellerid=request.session['id']
    sellerid_obj=sellerregister_tb.objects.get(id=sellerid)
    seller=product_tb(productname=productname,file=image,price=price,details=details,stock=stock,category=category_obj,sellerid=sellerid_obj)
    seller.save()
    messages.add_message(request,messages.INFO,"added successfully")
    return redirect('addproduct')
def viewProduct(request):
    sellerid=request.session['id']
    product=product_tb.objects.filter(sellerid=sellerid)
    return render(request,'viewProduct.html',{'data':product})
def delete(request,uid):
    seller=product_tb.objects.filter(id=uid).delete()
    return redirect('viewProduct')
def edit(request,uid):
    product=product_tb.objects.filter(id=uid)
    category=category_tb.objects.all()
    return render(request,'edit.html',{'data':product,'category':category})
def editAction(request):
    productname=request.POST['productname']
    productid=request.POST['uid']
    product=product_tb.objects.filter(id=productid)
    
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image=product[0].file
    price=request.POST['price']
    details=request.POST['details']
    stock=request.POST['stock']
    category=request.POST['category']
    category_obj=category_tb.objects.get(id=category)
    seller=product_tb.objects.filter(id=productid).update(productname=productname,price=price,details=details,stock=stock,category=category_obj)
    productobject=product_tb.objects.get(id=productid)
    productobject.file=image
    productobject.save()
    messages.add_message(request,messages.INFO,"updated successfully")
    return redirect('viewproduct')
def viewcustomerOrder(request):
    sellerid=request.session['id']
    order=order_tb.objects.filter(sellerid=sellerid)
    
    return render(request,'viewcustomerOrder.html',{'data':order})
def confirm(request,uid):
    seller=order_tb.objects.filter(id=uid).update(status='confirm')
    return redirect('viewcustomerOrder')
def reject(request,uid):
    seller=order_tb.objects.filter(id=uid).update(status='reject')
    return redirect('viewcustomerOrder')
def confirmCancellation(request,uid):
    product=order_tb.objects.filter(id=uid)
    product.update(status='Cancellation successfull')
    product1=product[0].productid
    productid=product1.id
    quantity=product[0].quantity
    print(quantity)
    productid_obj=product_tb.objects.filter(id=productid)
    stock=productid_obj[0].stock
    stocknew=stock+quantity
    productid_obj.update(stock=stocknew)
    return redirect('viewcustomerOrder')
def addtrackingDetails(request,uid):
    seller=order_tb.objects.filter(id=uid)
    return render(request,'addtrackingDetails.html',{'data':seller})
def addtrackingDetailsAction(request):
    orderid=request.POST['uid']
    orderid_obj=order_tb.objects.get(id=orderid)
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%m")
    seller=tracking_tb(orderid=orderid_obj,details=details,date=date,time=time)
    seller.save()
    detailslower=details.lower()
    if 'delivered' in detailslower:
        order=order_tb.objects.filter(id=orderid).update(status='delivered')
    messages.add_message(request,messages.INFO,"added tracking details")
    return redirect('viewcustomerOrder')
def sellerupdateProfile(request):
    sellerid=request.session['id']
    seller=sellerregister_tb.objects.filter(id=sellerid)
    return render(request,'sellerupdateProfile.html',{'data':seller})
def sellerupdateProfileAction(request):
    sellerid=request.session['id']
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    phone=request.POST['phone']
    address=request.POST['address']
    username=request.POST['username']
    seller=sellerregister_tb.objects.filter(id=sellerid)
    print(seller)
    if len(request.FILES)>0:
        image=request.FILES['proofupload']
    else:
        proofupload=seller[0].proofupload
    seller=sellerregister_tb.objects.filter(id=sellerid).update(name=name,dob=dob,gender=gender,country=country,phone=phone,address=address,username=username,proofupload=image)
    messages.add_message(request,messages.INFO,"updatedprofile")
    return redirect('sellerupdateProfile')
    
    



    
            
    
