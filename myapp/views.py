from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . froms import MyStdRegFrm, UserRegFrm, UserLoginFrm
from . models import Student, Product, Category

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return redirect('/user-log')

def about(request):
    allCate=Category.objects.all()
    allProd=Product.objects.all()
    return render(request, 'myapp/about.html', {'allProd':allProd, 'allCate':allCate})

def stdreg(request):
    if request.POST:
        frm=MyStdRegFrm(data=request.POST)
        if frm.is_valid():
            try:
                frm.save()
                messages.success(request, 'Student data save successfully')
            except Exception as e:
                messages.error(request, e)
    else:
        frm=MyStdRegFrm()
    context={'frm':frm}
    return render(request, 'myapp/reg.html', context)

def viewStd(request):
    allStd=Student.objects.all()
    context={'allStd':allStd}
    return render(request, 'myapp/viewStd.html', context)

def delStd(request,sid):
    try:
        Student.objects.filter(sid=sid).delete()
        # "DELETE FROM student WHERE sid=sid"
        messages.success(request, 'Student details delete successfully')
        return redirect('/stdview')
    except Exception as e:
        messages.error(request, 'Student details not delete successfully')
        return redirect('/stdview')
    

def updStd(request,sid):
    std=Student.objects.get(sid=sid)
    if request.POST:
        frm=MyStdRegFrm(request.POST or None, instance=std)
        if frm.is_valid():
            try:
                frm.save()
                messages.success(request, 'Sutdent details update successfully')
                return redirect('/stdview')
            except Exception as e:
                messages.error(request, 'Sutdent details not update successfully')
                return redirect('/stdview')
    else:
        frm=MyStdRegFrm(instance=std)
    context={'frm':frm}
    return render(request, 'myapp/updStd.html', context={'frm':frm})

def prdDetails(request, pid):
    allProd=Product.objects.filter(p_id=pid)
    return render(request, 'myapp/product.html', {'allProd':allProd})

def cateDetails(request, catid):
    allCate=Category.objects.all()
    allProd=Product.objects.filter(category=catid)
    return render(request, 'myapp/about.html', {'allProd':allProd, 'allCate':allCate})

def userReg(request):
    if request.POST:
        frm=UserRegFrm(data=request.POST)
        if frm.is_valid():
            try:
                frm.save()
                messages.success(request, 'Your registration successfull')
            except Exception as e:
                messages.error(request, 'Your registration is not successfull')
    else:
        frm=UserRegFrm()
    context={'frm':frm}
    return render(request, 'myapp/reg1.html', context)

def userLogin(request):
    if request.POST:
        frm=UserLoginFrm(request=request, data=request.POST)
        if frm.is_valid():
            uname=frm.cleaned_data['username']
            upass=frm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
    frm=UserLoginFrm()
    context={'frm':frm}
    return render(request, 'myapp/log.html', context)

def userLogout(request):
    logout(request)
    return redirect('/user-log')