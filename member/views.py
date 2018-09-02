import logging
import random

from django.db import DatabaseError
from django.shortcuts import render, get_object_or_404

# Create your views here.
from member.models import GoodsType, Goods


def show_goods(request):
    all_types = GoodsType.objects.all()
    goods_list = []
    for type in all_types:
        b={}
        b['type'] = type.title
        goods_type = get_object_or_404(GoodsType,title=type.title)
        goods = random.sample(list(goods_type.goods_set.all()),3)
        b['goods'] = goods
        goods_list.append(b)
    return render(request,"index.html",locals())

def show_detail(request):
    goodid = request.GET.get("goodid")
    try:
        good = Goods.objects.filter(id=goodid)
    except DatabaseError as e:
        logging.warning(e)
    return render(request,'detail.html',{"good":good[0]})

















