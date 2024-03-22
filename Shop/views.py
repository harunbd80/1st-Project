from django.shortcuts import render
from django.views import View
from . models import  product,customer
from . forms import CustomerRegistrationForm,customerprofile
from django.contrib import messages

# Create your views here.
class productView(View):
  def get(self,request):
     pants=product.objects.filter(cetagory='P')
     shirt=product.objects.filter(cetagory='sh')
     jercy=product.objects.filter(cetagory='j')
     saree=product.objects.filter(cetagory='s')
     lehenga=product.objects.filter(cetagory='k')
 
     return render(request, 'Shop/home.html',{'pant':pants,'shirt':shirt,'jercy':jercy,'sare':saree,'lahenga':lehenga})

class productDetialView(View):
 def get(self,request,pk):
   product_detail=product.objects.get(pk=pk)
   return render(request, 'Shop/productdetail.html',{'produc_d':product_detail})

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

class customerprofileView(View):
 def get (self,request):
  form=customerprofile()
  return render(request, 'Shop/profile.html',{'form':form,'active':'btn-primary'})
 
 def post(self,request):
   form=customerprofile(request.POST)
   if form.is_valid():
    usr=request.user
    name=form.cleaned_data['name']
    division=form.cleaned_data['division']
    district=form.cleaned_data['district']
    thana=form.cleaned_data['thana']
    vilroad=form.cleaned_data['vllorroad']
    zipcode=form.cleaned_data['zipcode']

    reg=customer(user=usr,name=name,division=division,district=district,thana=thana,vllorroad=vilroad,zipcode=zipcode)

    reg.save()
    messages.success(request,'Succesfully Done your Profile')
   return render(request, 'Shop/profile.html',{'form':form,'active':'btn-primary'})



def address(request):
 add=customer.objects.filter(user=request.user)
 
 return render(request, 'Shop/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request,data=None):
 if data==None:
   lehengas=product.objects.filter(cetagory='k')
 elif data=='Arong' or data=='Sara':
   lehengas=product.objects.filter(cetagory='k').filter(brand=data)
 return render(request, 'Shop/lehenga.html',{'lehanga':lehengas})

def login(request):
     return render(request, 'Shop/login.html')

class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'Shop/customerregistration.html', {'form': form})
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   form.save()
   messages.success(request,'Congratuolation Succesfully Registration Done!!!')
  return render(request, 'Shop/customerregistration.html',{'form': form})
  

def checkout(request):
 return render(request, 'Shop/checkout.html')
