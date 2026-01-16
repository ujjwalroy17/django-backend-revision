from django.contrib import admin
from student.models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','email','city')
    
admin.site.register(Profile,ProfileAdmin)

# Two different ways to register 

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','subject','marks')
    
