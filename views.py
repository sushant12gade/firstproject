from django.contrib import auth
from django.contrib.messages.api import error
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request, 'home.html')

def handleSignup(request):
      if request.method == 'POST':
             
         username = request.POST['username']
         fname = request.POST['fname']
         lname = request.POST['lname']
         email  = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']

         # chck erroes
         if  password1 != password2:
            messages.error(request, "passwords doesnt match")   
            return redirect( 'home')

         if not username.isalnum():
            messages.error(request, "username is not alphanumeric")   
            return redirect( 'home')
              
          

         myuser = User.objects.create_user(username, email, password1)
         myuser.first_name= fname
         myuser.last_name= lname
         myuser.save()
         messages.success(request, "your  account has been succesful created")

         # value error comes when redirect is npt taken
         return redirect( 'home')


      else:
        return HttpResponse('404 - noty found')     

def handleLogin(request):
    if request.method == 'POST':
             
       loginusername = request.POST['loginusername']
       loginpassword = request.POST['loginpassword']

    user = authenticate(username=loginusername, password=loginpassword)
    if user:
       login(request,user)
       if user.is_superuser:
         return HttpResponseRedirect("/admin")
       if user is not None:
         login(request, user )
         messages.success(request, " loged in sucessful")
         return redirect('profile')
       else:
         messages.error(request, " loged in unsucessful please tryagain ")   
         return redirect('home') 

       
         



           
    
    return HttpResponse('404-not found')
     
def handleLogout(request):
   
   logout(request)
   messages.success(request, " loged out ")
   return redirect('home')

def profile(request):
   return render(request, 'profile.html')


@login_required()
def editprofile(request):
       




       if request.method == 'POST':
             
         
         fn = request.POST['fname']
         ln = request.POST['lname']
         em  = request.POST['email']
         un = request.POST['uname']
        

        
              
          

         myuser = User.objects.get(id=request.user.id)
         myuser.first_name= fn
         myuser.last_name= ln
         myuser.username=un
         myuser.email=em
         myuser.save()
         messages.success(request, "your  changes done sucessfully!!!")

        
         return redirect( 'home')



       else:
        return render(request,'editprofile.html')  