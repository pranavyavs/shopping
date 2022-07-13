from django.db import models

# Create your models here.
class buyer_tb(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class cart_tb(models.Model):
    productid=models.ForeignKey('site_seller.product_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey('site_buyer.buyer_tb',on_delete=models.CASCADE)
    shippingadress=models.CharField(max_length=20)
    contactno=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
class order_tb(models.Model):
    productid=models.ForeignKey('site_seller.product_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey('site_buyer.buyer_tb',on_delete=models.CASCADE)
    sellerid=models.ForeignKey('site_seller.sellerregister_tb',on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')
    
    
