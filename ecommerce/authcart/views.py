from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is not matching")
            return render(request,'signup.html')
        
        try:
            if User.objects.get(username=email):
                return HttpResponse("email already exist")
                #return render(request,'auth/signup.html')
            
        except Exception as identefier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User Created",email)

    return render(request,"signup.html")

def handlelogin(request):
    if request.method=='POST':

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,'/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')