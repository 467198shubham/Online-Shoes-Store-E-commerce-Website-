from django.contrib import admin
from Myadmin.models import Category,Shoes

# Register your models here.
class  CategoryAdmin(admin.ModelAdmin):
    list_display=['cname']
    
class ShoesAdmin(admin.ModelAdmin):
    list_display=['shoesName','price','description','category','imageurl']
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Shoes,ShoesAdmin)
