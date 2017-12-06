from django.conf.urls import  url
from . import views
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name= 'home_page' ),
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name= 'login' ),
    url(r'logout/$', auth_views.LogoutView.as_view(), name= 'logout' ),
    url(r'signup/$', views.CreateUser.as_view(), name= 'signup' ),


]
