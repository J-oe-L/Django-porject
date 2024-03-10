
from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})

def alldetails(request,c):
    p=Product.objects.get(name=c)
    return render(request,'detail.html',{'p':p})

def register(request):
    if(request.method=="POST"):
        j = request.POST['j']
        o = request.POST['o']
        e = request.POST['e']
        s = request.POST['s']
        a = request.POST['a']
        l = request.POST['l']

        if(o==e):
            user = User.objects.create_user(username=j,password=o,first_name=s,last_name=a,email=l)
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse("password are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        j = request.POST['j']
        o = request.POST['o']
        user = authenticate(username=j,password=o)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)




