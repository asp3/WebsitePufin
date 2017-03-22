from django.contrib import admin
from .models import UserInfo

class UserAdmin(admin.ModelAdmin):
    fields = ['Orig_Platform', 'Orig_Loanid', 'Orig_Loanamount', 'Orig_Loandate', 'Published', 'upload']
    list_display = ['Orig_Platform', 'Orig_Loanid', 'Orig_Loanamount', 'Orig_Loandate', 'Published', 'upload']

    def Orig_Platform(self,obj):
        return obj.user.Orig_Platform

    def Orig_Loanid(self,obj):
        return obj.user.Orig_Loanid

    def Orig_Loanamount(self,obj):
        return obj.user.Orig_Loanamount

    def Orig_Loandate(self,obj):
        return obj.user.Orig_Loandate

    def Published(self,obj):
        return obj.user.Published

    def upload(self,obj):
	return obj.user.upload

admin.site.register(UserInfo, UserAdmin)
