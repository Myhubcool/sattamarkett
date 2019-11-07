from django.db import models
from datetime import datetime   

class gamesection(models.Model):
    gamedate=models.DateTimeField(default=datetime.now(), blank=True)
    gameno=models.CharField(max_length=5)    

    def __str__(self):
        return self.gameno

class adminaccount(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)    

    def __str__(self):
        return self.username

class payno(models.Model):
    paytmno=models.CharField(max_length=10)

class adminrequest(models.Model):
    userid=models.CharField(max_length=50)
    useramount=models.CharField(max_length=50)
    def __str__(self):
        return self.useramount


class singlerate(models.Model):
    gname=models.CharField(max_length=10)
    gfirst=models.CharField(max_length=10)
    gfirstp=models.CharField(max_length=10)
    gsecond=models.CharField(max_length=10)
    gsecondp=models.CharField(max_length=10)
    gthird=models.CharField(max_length=10)
    gthirdp=models.CharField(max_length=10)
    gfour=models.CharField(max_length=10)
    gfourp=models.CharField(max_length=10)
    gfive=models.CharField(max_length=10)
    gfivep=models.CharField(max_length=10)

    def __str__(self):
        return self.gname      

class joddirate(models.Model):
    gname=models.CharField(max_length=10)
    gfirst=models.CharField(max_length=10)
    gfirstp=models.CharField(max_length=10)
    gsecond=models.CharField(max_length=10)
    gsecondp=models.CharField(max_length=10)
    gthird=models.CharField(max_length=10)
    gthirdp=models.CharField(max_length=10)
    gfour=models.CharField(max_length=10)
    gfourp=models.CharField(max_length=10)
    gfive=models.CharField(max_length=10)
    gfivep=models.CharField(max_length=10)

    def __str__(self):
        return self.gname       


class doublerate(models.Model):
    gname=models.CharField(max_length=10)
    gfirst=models.CharField(max_length=10)
    gfirstp=models.CharField(max_length=10)
    gsecond=models.CharField(max_length=10)
    gsecondp=models.CharField(max_length=10)
    gthird=models.CharField(max_length=10)
    gthirdp=models.CharField(max_length=10)
    gfour=models.CharField(max_length=10)
    gfourp=models.CharField(max_length=10)
    gfive=models.CharField(max_length=10)
    gfivep=models.CharField(max_length=10)

    def __str__(self):
        return self.gname       

class triplerate(models.Model):
    gname=models.CharField(max_length=10)
    gfirst=models.CharField(max_length=10)
    gfirstp=models.CharField(max_length=10)
    gsecond=models.CharField(max_length=10)
    gsecondp=models.CharField(max_length=10)
    gthird=models.CharField(max_length=10)
    gthirdp=models.CharField(max_length=10)
    gfour=models.CharField(max_length=10)
    gfourp=models.CharField(max_length=10)
    gfive=models.CharField(max_length=10)
    gfivep=models.CharField(max_length=10)

    def __str__(self):
        return self.gname       