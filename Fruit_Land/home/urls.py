from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('xyz/',views.test1),
    path('login/',views.login,name="logpage"),
    path('register/',views.register,name="regpage"),
    path('logout/',views.logout)
   
]