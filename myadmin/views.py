from django.shortcuts import render
from .models import adminaccount , gamesection, singlerate, joddirate, doublerate, triplerate, payno , adminrequest
from user.models import umanagedata , userwallet

def persninfo(request):
    if request.method == 'POST':
        pytm = request.POST['pytm']
        adddata=payno()
        adddata.paytmno=pytm
        adddata.save()
        return render(request,'myadmin/persninfo.html',{'success':'You have Changed Paytm Number'})
    else:
        return render(request,'myadmin/persninfo.html')

def sendreq(request):
    if request.method == 'POST':
        amt = request.POST['amt']
        userid = request.POST['userid']
        adddata=adminrequest()        
        adddata.userid=userid
        userdta=userwallet.objects.all()            
        for data in userdta:
            if data.userid==userid:
                num1=data.useramt
                num2=amt
                added=int(num1)+int(num2)
                add2=str(added)
                adddata.useramount=add2
                userwallet.objects.filter(userid=userid).update(useramt=add2)
                adddata.save()        
        return render(request,'myadmin/sendreq.html',{'success':'You have send virtual money to ','userid':userid})
    else:
        return render(request,'myadmin/sendreq.html')    

def tgameupload(request):
    if request.method=='POST':
        triplerate.objects.filter(gname='triple').update(gfirst=request.POST['gfirst'],gfirstp=request.POST['gfirstp'],
        gsecond=request.POST['gsecond'],gsecondp=request.POST['gsecondp'],gthird=request.POST['gthird'],
        gthirdp=request.POST['gthirdp'],gfour=request.POST['gfour'],gfourp=request.POST['gfourp'],
        gfive=request.POST['gfive'],gfivep=request.POST['gfivep'])        
        dataa=triplerate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/triplepatti.html',{'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/tgameupload.html')    

def dgameupload(request):
    if request.method=='POST':
        doublerate.objects.filter(gname='double').update(gfirst=request.POST['gfirst'],gfirstp=request.POST['gfirstp'],
        gsecond=request.POST['gsecond'],gsecondp=request.POST['gsecondp'],gthird=request.POST['gthird'],
        gthirdp=request.POST['gthirdp'],gfour=request.POST['gfour'],gfourp=request.POST['gfourp'],
        gfive=request.POST['gfive'],gfivep=request.POST['gfivep'])        
        dataa=doublerate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/doublepatti.html',{'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/dgameupload.html')    

def sgameupload(request):
    if request.method=='POST':
        singlerate.objects.filter(gname='single').update(gfirst=request.POST['gfirst'],gfirstp=request.POST['gfirstp'],
        gsecond=request.POST['gsecond'],gsecondp=request.POST['gsecondp'],gthird=request.POST['gthird'],
        gthirdp=request.POST['gthirdp'],gfour=request.POST['gfour'],gfourp=request.POST['gfourp'],
        gfive=request.POST['gfive'],gfivep=request.POST['gfivep'])        
        dataa=singlerate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/singlepatti.html',{'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/sgameupload.html')
    
def jgameupload(request):
    if request.method=='POST':
        joddirate.objects.filter(gname='joddi').update(gfirst=request.POST['gfirst'],gfirstp=request.POST['gfirstp'],
        gsecond=request.POST['gsecond'],gsecondp=request.POST['gsecondp'],gthird=request.POST['gthird'],
        gthirdp=request.POST['gthirdp'],gfour=request.POST['gfour'],gfourp=request.POST['gfourp'],
        gfive=request.POST['gfive'],gfivep=request.POST['gfivep'])        
        dataa=joddirate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/joddipatti.html',{'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/jgameupload.html')

def ahome(request):    
    if request.method=='POST':        
        admindatack=adminaccount.objects.all()            
        for data in admindatack:            
            if data.username == request.POST['username'] and data.password == request.POST['password1']:                
                return render(request,'myadmin/amainhome.html')                
        else:
            return render(request,'myadmin/ahome.html',{'error':'Your username or password is wrong!'})                        
    else:        
        return render(request,'myadmin/ahome.html')        

def amainhome(request):
    if request.method=='POST':
        data=gamesection()
        data.gameno=request.POST['gameno']
        gameno=request.POST['gameno']        
        data.save()
        return render(request,'myadmin/amainhome.html',{'success':'Today game number is ','gameno':gameno})
    else:
        return render(request,'myadmin/amainhome.html')

def allplayer(request):
    if request.method=='POST':
            print('hello')
    else:
        data=umanagedata.objects.all()
        return render(request,'myadmin/allplayer.html',{'data':data})

def singlepatti(request):
    if request.method=='POST':
        gname=request.POST['gname']
        dataa=singlerate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/singlepatti.html',{'gname':gname,'dataa':dataa,'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/singlepatti.html',{'dataa':dataa})

def joddipatti(request):
    if request.method=='POST':
        gname=request.POST['gname']
        dataa=joddirate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/joddipatti.html',{'gname':gname,'dataa':dataa,'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/joddipatti.html',{'dataa':dataa})

def doublepatti(request):
    if request.method=='POST':
        gname=request.POST['gname']
        dataa=doublerate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/doublepatti.html',{'gname':gname,'dataa':dataa,'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/doublepatti.html',{'dataa':dataa})

def triplepatti(request):
    if request.method=='POST':
        gname=request.POST['gname']
        dataa=triplerate.objects.all()
        for sett in dataa:
            gfirst=sett.gfirst
            gfirstp=sett.gfirstp
            gsecond=sett.gsecond
            gsecondp=sett.gsecondp
            gthird=sett.gthird
            gthirdp=sett.gthirdp
            gfour=sett.gfour
            gfourp=sett.gfourp
            gfive=sett.gfive
            gfivep=sett.gfivep            
        return render(request,'myadmin/triplepatti.html',{'gname':gname,'dataa':dataa,'gfirst':gfirst,'gfirstp':gfirstp,'gsecond':gsecond,
        'gsecondp':gsecondp,'gthird':gthird,'gthirdp':gthirdp,'gfour':gfour,'gfourp':gfourp,'gfive':gfive,'gfivep':gfivep})
    else:        
        return render(request,'myadmin/triplepatti.html',{'dataa':dataa})