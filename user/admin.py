from django.contrib import admin
from .models import useraccount , umanagedata, userwallet
admin.site.register(useraccount)
admin.site.register(userwallet)
admin.site.register(umanagedata)