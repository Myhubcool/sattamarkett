from django.db import models
from datetime import datetime   

class useraccount(models.Model):
    username=models.CharField(max_length=50)
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=12)
    email=models.CharField(max_length=50)

    def __str__(self):
        return self.userid

class userwallet(models.Model):
    useramt=models.CharField(max_length=20)
    userid=models.CharField(max_length=50)

    def __str__(self):
        return self.userid

class umanagedata(models.Model):
    userid=models.CharField(max_length=50)
    gameno=models.CharField(max_length=50)
    gamename=models.CharField(max_length=50)
    price=models.CharField(max_length=15)        
    date=models.DateTimeField(default=datetime.now(), blank=True)
    usersc=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.userid
