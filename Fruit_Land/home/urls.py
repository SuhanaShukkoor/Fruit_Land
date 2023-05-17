from django.urls import path
from . import views
from . import feed

urlpatterns = [
    path('',views.index,name="homepage"),
    path('xyz/',views.test1),
    path('login/',views.login,name="logpage"),
    path('register/',views.register,name="regpage"),
    path('logout/',views.logout),
    path('feed/',feed.latest()),
    path('search/',views.search),
    path('search/searchsub/',views.searchsub)
   
]