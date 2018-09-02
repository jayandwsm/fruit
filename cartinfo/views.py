import datetime
import json
import logging

from django.db import DatabaseError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import date

from cartinfo.models import CartInfo, Order
from member.models import Goods
from userinfo.models import UserInfo, Address


def addcart(request):
    goodid = request.GET.get("goodid")
    gcount = request.GET.get("gcount")
    userid = request.session.get("user_id")
    check_goods = Goods.objects.filter(id=goodid)
    check_user = UserInfo.objects.filter(id=userid)
    new_cart = CartInfo()
    if len(check_goods) <= 0:
        message = {"error":"商品不存在"}
        return HttpResponse(json.dumps(message))
    else:
        new_cart.user = check_user[0]
        new_cart.goods = check_goods[0]
        new_cart.ccount = gcount
        try:
            check_cart = CartInfo.objects.filter(goods_id=goodid,user_id=userid)
            if len(check_cart) <= 0:
                new_cart.save()
            else:
                check_cart[0].ccount = int(gcount) + check_cart[0].ccount
                check_cart[0].save()
        except DatabaseError as e:
            logging.warning(e)
        return HttpResponse(json.dumps({"success":"加入成功"}))

def order(request):
    # 1.获取用户id
    userid = request.session.get("user_id")
    # uname = request.session.get("uname")
    # 2.查询购物车中的数据返回给order.html
    cart_goods = CartInfo.objects.filter(user_id=userid)
    # print(cart_goods)
    # 3.获取客户地址
    goods_address = Address.objects.filter(user_id=userid)
    # print(goods_address)
    return render(request,"order.html",locals())

def add_order(request):
    # 1.从前段页面获取订单号、订单细节、收件人姓名、收件人电话、地址、总数、总价
    # 获取用户id并查询出user
    userid = request.session.get("user_id")
    orderNo = datetime.datetime.now().strftime('%y%m%d%h%m%s')
    orderdetail = request.POST.get('desc')
    adsname = request.POST.get('adsname')
    adsphone = request.POST.get('adsphone')
    ads = request.POST.get('ads')
    acot = 100
    acount = 1100
    print(userid,orderNo,orderdetail,adsname,adsphone,ads)
    user = UserInfo.objects.get(id=userid)
    print(orderdetail)
    #或者再次查询数据库
    # 2.存进数据库
    try:
        order = Order.objects.create(orderNo=orderNo,orderdetail=orderdetail,
                                 adsname=adsname,adsphone=adsphone,ads=ads,
                                 acot=acot,acount=acount,user=user)
    except DatabaseError as e:
        logging.warning(e)
    # 3.返回存储成功显示给客户并调回主页
    return HttpResponse(json.dumps({"success": "OK"}))
