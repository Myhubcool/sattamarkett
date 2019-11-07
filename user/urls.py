from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),    
    path('register',views.register,name='register'),
    path('loggedin',views.mainhome,name='mainhome'),
    path('playedgame',views.playedgame,name='playedgame'),
    path('home/trending',views.trending,name='trending'),
    path('home/singletemp',views.singletemp,name='singletemp'),   
    path('home/jodditemp',views.jodditemp,name='jodditemp'),   
    path('home/doubletemp',views.doubletemp,name='doubletemp'),   
    path('home/tripletemp',views.tripletemp,name='tripletemp'),   
    path('home/single',views.single,name='single'), 
    path('home/change',views.change,name='change'),
    path('home/joddi',views.joddi,name='joddi'),
    path('home/triple',views.triple,name='triple'),
    path('home/double',views.double,name='double'), 
]