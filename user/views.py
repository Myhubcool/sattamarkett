from django.shortcuts import render
from .models import useraccount , umanagedata , userwallet
from myadmin.models import gamesection , singlerate , joddirate, doublerate, triplerate,payno,adminrequest

def home(request):
    if request.method=='POST':        
        userdatack=useraccount.objects.all()            
        for data in userdatack:            
            if data.username == request.POST['username'] and data.password == request.POST['password1']:
                userid=data.userid
                gameno=gamesection.objects.all()                
                for no in gameno:
                    gno=no.gameno               
                daata=userwallet.objects.all()                                
                for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt                         
                return render(request,'user/mainhome.html',{'userid':userid,'gno':gno,'useramt':useramt})                
        else:
            return render(request,'user/home.html',{'error':'Your username or password is wrong!'})                        
    else:        
        return render(request,'user/home.html')

def forgotpassword(request):
    if request.method=='POST':
        usercheckdata=useraccount.objects.all()                
        for data in usercheckdata:
            if data.username==request.POST['username'] and data.mobileno==request.POST['mobileno'] and data.email==request.POST['email']:
                userid=data.userid
                oldpassword=data.password                
                return render(request,'user/changepassword.html',{'userid':userid,'oldpassword':oldpassword})
        else:
            usercheckdata=useraccount.objects.all()    
            for data in usercheckdata:
                if data.username!=request.POST['username']:
                    return render(request,'user/forgotpassword.html',{'error':'Username is not correct'})
                elif data.mobileno!=request.POST['mobileno']:
                    return render(request,'user/forgotpassword.html',{'error':'Mobile Number is not correct'})
                elif data.email!=request.POST['email']:
                    return render(request,'user/forgotpassword.html',{'error':'Email ID is not correct'})                            
    else:
        return render(request,'user/forgotpassword.html')

def register(request):
    if request.method=='POST':
        if request.POST['password1'] == request.POST['password2']:
            userdatack=useraccount.objects.all()            
            userinfo=useraccount()
            mob=request.POST['mobileno']         
            mobb=mob[2:8:2]   
            useridd=request.POST['username']+str(mobb)            
            for data in userdatack:                
                    if data.userid == useridd:
                        return render(request,'user/register.html',{'error':'This userid is not available please try another name'})            
                    elif data.mobileno == request.POST['mobileno']:
                        return render(request,'user/register.html',{'error':'This mobile number is already registered please try another one'})            
                    elif data.email == request.POST['email']:
                        return render(request,'user/register.html',{'error':'This email id is already registered please try another one'})            
            else:                                
                userinfo.username=request.POST['username']
                userinfo.password=request.POST['password1']
                userinfo.confirm_password=request.POST['password2']
                userinfo.email=request.POST['email']
                userinfo.mobileno=request.POST['mobileno']
                mob=request.POST['mobileno']         
                mobb=mob[2:8:2]   
                useridd=request.POST['username']+str(mobb)
                userinfo.userid=useridd
                userid=useridd                
                datata=userwallet()
                datata.userid=userid
                datata.useramt='100'                
                datata.save()
                gameno=gamesection.objects.all()                               
                for no in gameno:
                    gno=no.gameno                
                userinfo.save()
                daata=userwallet.objects.all()                                
                for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt
                        return render(request,'user/mainhome.html',{'userid':userid,'gno':gno,'useramt':useramt})          
                else:
                    useramt='100'                
                    return render(request,'user/mainhome.html',{'userid':userid,'gno':gno,'useramt':useramt})          
        else:
            return render(request,'user/register.html',{'error':'Your password is not matching with confirm-password'})
    else:    
        return render(request,'user/register.html')

def mainhome(request):
    if request.method=='POST':
        userid=request.POST['userid']
        gameno=gamesection.objects.all()
        for no in gameno:
            gno=no.gameno   
        daata=userwallet.objects.all()                                
        for dt in daata:
                if userid == dt.userid:
                     useramt=dt.useramt                         
        return render(request,'user/mainhome.html',{'userid':userid,'gno':gno,'useramt':useramt})    
    else:
        gameno=gamesection.objects.all()
        for no in gameno:
            gno=no.gameno   
        userid=request.POST['userid']
        daata=userwallet.objects.all()                                
        for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt                         
        return render(request,'user/mainhome.html',{'userid':userid,'gno':gno,'useramt':useramt})    
    
def playedgame(request):
    if request.method=='POST':        
            userid=request.POST['userid']    
            data=umanagedata.objects.all()        
            daata=userwallet.objects.all()                                
            for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt                         
            return render(request,'user/playedgame.html',{'userid':userid,'data':data,'useramt':useramt})
    else:
        userid=request.POST['userid']          
        daata=userwallet.objects.all()                                
        for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt                         
        return render(request,'user/playedgame.html',{'userid':userid,'useramt':useramt})  
   
def trending(request):
    if request.method=='POST':
        userid=request.POST['userid']
        sdata=singlerate.objects.all()
        jdata=joddirate.objects.all()
        ddata=doublerate.objects.all()
        tdata=triplerate.objects.all()
        daata=userwallet.objects.all()                                
        for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt                         
        return render(request,'user/trending.html',{'useramt':useramt,'userid':userid,'sdata':sdata,'jdata':jdata,'ddata':ddata,'tdata':tdata})
    else:
        userid=request.POST['userid']
        daata=userwallet.objects.all()                                
        for dt in daata:
                    if userid == dt.userid:
                        useramt=dt.useramt                         
        return render(request,'user/trending.html',{'userid':userid,'useramt':useramt})
        
def singletemp(request):
    if request.method=='POST':                    
            userid=request.POST['userid']                   
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt
            pyno=payno.objects.all()
            for pn in pyno:
                pytn=pn.paytmno                                                 
            return render(request,'user/single.html',{'userid':userid,'useramt':useramt,'pytn':pytn})  
    else:                
        daata=userwallet.objects.all()                         
        for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                         
        userid=request.POST['userid']                    
        return render(request,'user/single.html',{'userid':userid,'useramt':useramt})  
    
def jodditemp(request):
    if request.method=='POST':        
            userid=request.POST['userid'] 
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                                
            pyno=payno.objects.all()
            for pn in pyno:
                pytn=pn.paytmno     
            return render(request,'user/joddi.html',{'userid':userid,'useramt':useramt,'pytn':pytn})  
    else:
        daata=userwallet.objects.all()                         
        for dt in daata:
                if userid == dt.userid:
                    useramt=dt.useramt                     
        userid=request.POST['userid']            
        return render(request,'user/joddi.html',{'userid':userid,'useramt':useramt})

def doubletemp(request):
    if request.method=='POST':        
            userid=request.POST['userid']            
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                                     
            pyno=payno.objects.all()
            for pn in pyno:
                pytn=pn.paytmno     
            return render(request,'user/double.html',{'userid':userid,'useramt':useramt,'pytn':pytn})  
    else:
        userid=request.POST['userid']            
        daata=userwallet.objects.all()                         
        for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                                     
        return render(request,'user/double.html',{'userid':userid,'useramt':useramt})                  

def tripletemp(request):
    if request.method=='POST':        
            userid=request.POST['userid']            
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                                     
            pyno=payno.objects.all()
            for pn in pyno:
                pytn=pn.paytmno     
            return render(request,'user/triple.html',{'userid':userid,'useramt':useramt,'pytn':pytn})  
    else:
            userid=request.POST['userid']            
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                                     
            return render(request,'user/triple.html',{'userid':userid,'useramt':useramt})                 

def single(request):
    if request.method=='POST':                                                        
            data=umanagedata()
            data.userid=request.POST['userid']
            userid=request.POST['userid']
            data.gameno=request.POST['gnumber']
            data.usersc=request.FILES['screenshort']
            data.price=request.POST['amount']
            data.gamename='Single'                        
            prc=request.POST['amount']
            price=int(prc)                        
            daata=userwallet.objects.all()                                     
            daataa=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramtt=dt.useramt                         
                        userintamt=int(useramtt)
                        newamt=userintamt-price
                        userwallet.objects.filter(userid=userid).update(useramt=newamt)       
                        data.save()     
            for dtt in daataa:
                if userid == dt.userid:
                    useramt=dt.useramt            
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                                     
            return render(request,'user/change.html',{'useramt':useramt,'success':'Congratulation your game is go on!','userid':userid})
    else:        
        return render(request,'user/single.html')             

def change(request):    
    return render(request,'user/change.html')

def double(request):
    if request.method=='POST':                                                        
            data=umanagedata()
            data.userid=request.POST['userid']
            userid=request.POST['userid']
            data.gameno=request.POST['gnumber']
            data.usersc=request.FILES['screenshort']
            data.price=request.POST['amount']
            data.gamename='Double'            
            prc=request.POST['amount']
            price=int(prc)                        
            daata=userwallet.objects.all()                         
            daataa=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramtt=dt.useramt                         
                        userintamt=int(useramtt)
                        newamt=userintamt-price
                        userwallet.objects.filter(userid=userid).update(useramt=newamt)       
                        data.save()     
            for dtt in daataa:
                if userid == dt.userid:
                    useramt=dt.useramt                        
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                         
            return render(request,'user/change.html',{"useramt":useramt,'success':'Congratulation your game is go on!','userid':userid})
    else:
        return render(request,'user/double.html')

def triple(request):
    if request.method=='POST':                                                        
            data=umanagedata()
            data.userid=request.POST['userid']
            userid=request.POST['userid']
            data.gameno=request.POST['gnumber']
            data.usersc=request.FILES['screenshort']
            data.price=request.POST['amount']
            data.gamename='Triple'            
            prc=request.POST['amount']
            price=int(prc)                        
            daata=userwallet.objects.all()                         
            daataa=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramtt=dt.useramt                         
                        userintamt=int(useramtt)
                        newamt=userintamt-price
                        userwallet.objects.filter(userid=userid).update(useramt=newamt)       
                        data.save()     
            for dtt in daataa:
                if userid == dt.userid:
                    useramt=dt.useramt            
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                         
            return render(request,'user/change.html',{"useramt":useramt,'success':'Congratulation your game is go on!','userid':userid})
    else:
        return render(request,'user/triple.html')

def joddi(request):
    if request.method=='POST':                                                        
            data=umanagedata()
            data.userid=request.POST['userid']
            userid=request.POST['userid']
            data.gameno=request.POST['gnumber']
            data.usersc=request.FILES['screenshort']
            data.price=request.POST['amount']
            data.gamename='Joddi'            
            prc=request.POST['amount']
            price=int(prc)                        
            daata=userwallet.objects.all()                         
            daataa=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramtt=dt.useramt                         
                        userintamt=int(useramtt)
                        newamt=userintamt-price
                        userwallet.objects.filter(userid=userid).update(useramt=newamt)       
                        data.save()     
            for dtt in daataa:
                if userid == dt.userid:
                    useramt=dt.useramt            
            daata=userwallet.objects.all()                         
            for dt in daata:
                if userid == dt.userid:
                        useramt=dt.useramt                         
            return render(request,'user/change.html',{"useramt":useramt,'success':'Congratulation your game is go on!','userid':userid})
    else:
        return render(request,'user/joddi.html')  
