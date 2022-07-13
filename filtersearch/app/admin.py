from django.contrib import admin

from . models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','creation_date','due_date']
admin.site.register(Task,TaskAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','release_date']
admin.site.register(Product,ProductAdmin)