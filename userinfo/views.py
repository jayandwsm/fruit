import logging

from django.contrib.auth.hashers import make_password,check_password
from django.db import DatabaseError
from django.shortcuts import render, redirect


# Create your views here.
from userinfo.models import UserInfo


def Login(request):
    return render(request,'login.html')
def Regist(request):
    return render(request,'regist.html')
def Regist_in(request):
    if request.method != 'POST':
        return redirect('/regist')
    else:
        new_user = UserInfo()
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        uphone = request.POST.get("uphone")
        upwd = request.POST.get("upwd")
        cupwd = request.POST.get("cupwd")
        if uname and email and uphone and upwd:
            check_uname = UserInfo.objects.filter(uname=uname)
            if len(check_uname) == 1:
                return render(request,"regist.html",{"message":"用户名已经存在"})
            else:
                new_user.uname = uname
                if upwd != cupwd:
                    return render(request,"regist.html",{"message":"两次密码不一致"})
                else:
                    new_user.upassword = make_password(upwd,'a','pbkdf2_sha256')
                    new_user.email = email
                    new_user.phone = uphone
                    try:
                        new_user.save()
                    except DatabaseError as e:
                        logging.warning(e)
                    return render(request,"index.html")
        else:
            return render(request, "regist.html", {"message": "有信息未填写"})

def Login_in(request):
    if request.method != 'POST':
        return redirect("/login")
    else:
        uname = request.POST.get("uname")
        upwd = request.POST.get("upwd")
        if uname and upwd:
            check_uname = UserInfo.objects.filter(uname=uname)
            if uname == check_uname[0].uname and check_password(upwd,check_uname[0].upassword):
                request.session['uname'] = uname
                request.session['user_id'] = check_uname[0].id
                return redirect('/index')
            else:
                return render(request, "login.html", {"message": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"message": "用户名或密码不能为空"})
def Login_out(request):
    if request.session:
        del request.session["uname"]
    return render(request,'index.html')