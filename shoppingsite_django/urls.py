"""shoppingsite_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from site_admin import views as adminview
from site_seller import views as sellerview
from site_buyer import views as buyerview
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',adminview.index,name='index'),
    url(r'^buyerregister/$',buyerview.buyerregister,name='buyerregister'),
    url(r'^registerAction/$',buyerview.buyerregisterAction,name='buyerregisterAction'),
    url(r'^sellerregister/$',sellerview.sellerregister,name='sellerregister'),
    url(r'^sellerregisterAction/$',sellerview.sellerregisterAction,name='sellerregisterAction'),
    url(r'^login/$',adminview.login,name='login'),
    url(r'^loginAction/$',adminview.loginAction,name='loginAction'),
    url(r'^checkUsername/$',sellerview.checkUsername,name='checkUsername'),
    url(r'^addcategory/$',adminview.addcategory,name='addcategory'),
    url(r'^addcategoryAction/$',adminview.addcategoryAction,name='addcategoryAction'),
    url(r'^viewAllSellers/$',adminview.viewAllSellers,name='viewAllSellers'),
    url(r'^approve/(?P<uid>\d+)/$',adminview.approve,name='approve'),
    url(r'^reject/(?P<uid>\d+)/$',adminview.reject,name='reject'),
    url(r'^addproduct/$',sellerview.addproduct,name='addproduct'),
    url(r'^addproductAction/$',sellerview.addproductAction,name='addproductAction'),
    url(r'^viewProduct/&',sellerview.viewProduct,name='viewProduct'),
    url(r'^delete/(?P<uid>\d+)/$',sellerview.delete,name='delete'),
    url(r'^edit/(?P<uid>\d+)/$',sellerview.edit,name='edit'),
    url(r'^editAction/$',sellerview.editAction,name='editAction'),
    url(r'^viewuserProduct/$',buyerview.viewuserProduct,name='viewuserProduct'),
    url(r'^addtocart/(?P<uid>\d+)$',buyerview.addtocart,name='addtocart'),
    url(r'^addtocartAction/$',buyerview.addtocartAction,name='addtocartAction'),
    url(r'^viewcart/$',buyerview.viewcart,name='viewcart'),
    url(r'^deletecart/(?P<uid>\d+)/$',buyerview.deletecart,name='deletecart'),
    url(r'^placeorderAction/$',buyerview.placeorderAction,name='placeorderAction'),
    url(r'^viewOrders/$',buyerview.viewOrders,name='viewOrders'),
    url(r'^cancel/(?P<uid>\d+)$',buyerview.cancel,name='cancel'),
    url(r'^viewcustomerOrder/$',sellerview.viewcustomerOrder,name='viewcustomerOrder'),
    url(r'^confirm/(?P<uid>\d+)$',sellerview.confirm,name='confirm'),
    url(r'^reject/(?P<uid>\d+)$',sellerview.reject,name='reject'),
    url(r'^confirmCancellation/(?P<uid>\d+)$',sellerview.confirmCancellation,name='confirmCancellation'),
    url(r'^addtrackingDetails/(?P<uid>\d+)$',sellerview.addtrackingDetails,name='addtrackingDetails'),
    url(r'^addtrackingDetailsAction/$',sellerview.addtrackingDetailsAction,name='addtrackingDetailsAction'),
    url(r'^viewtrackingDetails/(?P<uid>\d+)$',buyerview.viewtrackingDetails,name='viewtrackingDetails'),
    url(r'^searchProduct/$',buyerview.searchProduct,name='searchProduct'),
    url(r'^searchProductAction/$',buyerview.searchProductAction,name='searchProductAction'),
    url(r'^searchproductbycategoryandprice/&',buyerview.searchproductbycategoryandprice,name='searchproductbycategoryandprice'),
    url(r'^searchproductbycategoryandpriceAction/&',buyerview.searchproductbycategoryandpriceAction,name='searchproductbycategoryandpriceAction'),
    url(r'^updateProfile/$',buyerview.updateProfile,name='updateProfile'),
    url(r'^updateProfileAction/$',buyerview.updateProfileAction,name='updateProfileAction'),
    url(r'^sellerupdateProfile/$',sellerview.sellerupdateProfile,name='sellerupdateProfile'),
    url(r'^sellerupdateProfileAction/$',sellerview.sellerupdateProfileAction,name='sellerupdateProfileAction'),
    url(r'^logout/$',adminview.logout,name='logout'),
    url(r'^forgotpassword/$',adminview.forgotpassword,name='forgotpassword'),
    url(r'^forgotpasswordAction/$',adminview.forgotpasswordAction,name='forgotpasswordAction'),
    url(r'^forgotpassword2Action/$',adminview.forgotpassword2Action,name='forgotpassword2Action'),
    url(r'^forgotpassword3Action/$',adminview.forgotpassword3Action,name='forgotpassword3Action'),
    
    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
