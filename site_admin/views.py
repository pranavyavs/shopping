from django.shortcuts import render,redirect 
from site_admin.models import *
from site_seller.models import *
from site_buyer.models import *
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=register_tb.objects.filter(username=username,password=password)
    seller=sellerregister_tb.objects.filter(username=username,password=password)
    buyer=buyer_tb.objects.filter(username=username,password=password)
    if len(admin)>0:
        request.session['id']=admin[0].id
        return render(request,'adminhome.html',{'data':admin})
    elif len(seller)>0:
        status=seller[0].status
        if(status=='approved'):
            request.session['id']=seller[0].id
            return render(request,'sellerhome.html',{'data':seller})
        else:
            messages.add_message(request,messages.INFO,"waiting for approval")
            return redirect('login')
    elif len(buyer)>0:
        request.session['id']=buyer[0].id
        return render(request,'buyerhome.html',{'data':buyer})
    else:
         messages.add_message(request,messages.INFO,"Incorrrect username or password")
         return redirect('login')
def addcategory(request):
    return  render(request,'addcategory.html')
def addcategoryAction(request):
    categoryname=request.POST['categoryname']
    admin=category_tb(categoryname=categoryname)
    admin.save()
    return redirect('addcategory')
def viewAllSellers(request):
    seller=sellerregister_tb.objects.all()
    return render(request,'viewAllSellers.html',{'data':seller})
def approve(request,uid):
    seller=sellerregister_tb.objects.filter(id=uid).update(status='approved')
    return redirect('viewAllSellers')
def reject(request,uid):
    seller=sellerregister_tb.objects.filter(id=uid).update(status='rejected')
    return redirect('viewAllSellers')
def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"logout")
    return redirect('index')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotpasswordAction(request):
    username=request.POST['username']
    user=buyer_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    if len(user)>0:
        
        return render(request,'forgotpassword2.html',{'username':username})
    elif len(seller)>0:
        return render(request,'forgotpasswword2.html',{'username':username})
    else:
        messages.add_message(request,messages.INFO,"username does not exist")
    return redirect('forgotpassword')
def forgotpassword2Action(request):
    username=request.POST['username']
    country=request.POST['country']
    dob=request.POST['dob']
    phone=request.POST['phone']
    buyer=buyer_tb.objects.filter(username=username,country=country,dob=dob,phone=phone)
    seller=sellerregister_tb.objects.filter(username=username,country=country,dob=dob,phone=phone)
    if len(buyer)>0:
        return render(request,'forgotpassword3.html',{'username':username})
    elif len(seller)>0:
        return render(request,'forgotpassword3.html',{'username':username})
    else:
        messages.add_message(request,messages.INFO,"details not correct")
    return redirect('forgotpassword')
def forgotpassword3Action(request):
    username=request.POST['username']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if(newpassword==confirmpassword):
        buyer=buyer_tb.objects.filter(username=username)
        seller=sellerregister_tb.objects.filter(username=username)
        if(buyer.count()>0):
            password=buyer_tb.objects.filter(username=username).update(password=newpassword)
        else:
            password=seller_tb.objects.filter(username=username).update(password=newpassword)
    else:
        messages.add_message(request,messages.INFO,"password missmatch found")
    return redirect('login')
        

    



                                    
