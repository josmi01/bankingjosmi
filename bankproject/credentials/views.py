from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('login')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return(render(request,"login.html"))

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname = request.POST['last_name']
        email= request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                            last_name=lastname, email=email)
                user.save();

            return redirect('login')

        else:
            messages.info(request ,"password incorrect")
            return redirect('register')
        return redirect('/')
    return (render(request,"register.html"))

def account(request):
    if request.method =='POST':
        name=request.POST['name']
        dob = request.POST['date of birth']
        password=request.POST['password']
        age = request.POST['age']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch= request.POST['branch']
        account_type = request.POST['account_type']
        materials= request.POST['materials']
        user=auth.authenticate(username=name,password=password,dob=dob,age=age,email=email,address=address,district=district,branch=branch,account_type=account_type,materials=materials)
        if user is not None:
            auth.account(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('account')
    return(render(request,"account.html"))

def logout(request):
    auth.logout(request)
    return redirect('/')

