from django.conf.urls import url
from userinfo import views

urlpatterns = [
    url('^login/',views.Login,name='login'),
    url('^regist/',views.Regist,name='regist'),
    url('^regist_in/',views.Regist_in,name='registin'),
    url('^login_in/',views.Login_in,name='loginin'),
    url('^login_out/',views.Login_out,name='loginout'),
]