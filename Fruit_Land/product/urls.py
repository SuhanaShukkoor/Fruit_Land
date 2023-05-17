from django.urls import path
from . import views

urlpatterns = [
    path('',views.about),
    path('cmt/',views.comment),
    path('like/',views.like),
    path('autoc/',views.autoc,name="autos")

]