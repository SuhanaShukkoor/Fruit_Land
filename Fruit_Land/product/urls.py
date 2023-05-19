from django.urls import path
from . import views

urlpatterns = [
    path('',views.about2),
    path('cmt/',views.comment),
    path('like/',views.like),
    path('autoc/',views.autoc,name="autos"),
    

]