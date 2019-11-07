from django.urls import path
from . import views

urlpatterns=[
    path('',views.ahome,name='ahome'),    
    path('admin/amainhome',views.amainhome,name='amainhome'),
    path('admin/allplayer',views.allplayer,name='allplayer'),
    path('admin/singlepatti',views.singlepatti,name='singlepatti'),    
    path('admin/joddipatti',views.joddipatti,name='joddipatti'),
    path('admin/doublepatti',views.doublepatti,name='doublepatti'),
    path('admin/triplepatti',views.triplepatti,name='triplepatti'),
    path('admin/sgameupload',views.sgameupload,name='sgameupload'),
    path('admin/jgameupload',views.jgameupload,name='jgameupload'),            
    path('admin/dgameupload',views.dgameupload,name='dgameupload'),
    path('admin/tgameupload',views.tgameupload,name='tgameupload'),
    path('admin/persninfo',views.persninfo,name='persninfo'),
    path('admin/sendreq',views.sendreq,name='sendreq')
    
]