from django.conf.urls import url
from django.contrib import admin
from cartinfo import views

urlpatterns = [
    url(r"^addcart/",views.addcart,name="addcart"),
    url(r"^order/",views.order,name="order"),
    url(r"^add_order/",views.add_order,name="add_order")

]