from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def base(request):
   return render(request,'base.html')

def login(request):
   if request.method=='POST': 
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'base.html',{'name':username})
        else:
            return render(request,'login.html',{'text':' SORRRY!! cannot login'})
   return render(request,'login.html')
    
def register(request):
   if request.method=='POST':
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      reepass=request.POST['repassword']
      if (password==reepass):
         if User.objects.filter(username=username).exists():
          messages.info(request,'USERNAME ALREADY EXISTS')
          return render(request,'register.html',{'error':"Account already exists!!!"})
         elif User.objects.filter(email=email).exists():
          messages.info(request,"email already exits")
          return render(request,'register.html',{'error':"Email already exists!!!"})   
         else :
          user=User.objects.create_user(username=username,email=email,password=password)  
          user.save()
          user1=auth.authenticate(username=username,password=password)
          auth.login(request,user1)   
          return render(request,'base.html',{'name':username})  
      else:
        messages(request,'password not the same')   
        return redirect('register')  
   return render(request,'register.html')     

def logout(request):
    auth.logout(request)
    return redirect('base')