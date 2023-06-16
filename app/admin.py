from django.contrib import admin
from .models import *

class CustomAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','role','is_staff') 

class CategoryAdmin(admin.ModelAdmin):
    list_display=('slug','category_name','cat_image')

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','slug','product_name','images','stock','price','category','modified_date')
   

admin.site.register(CustomUser,CustomAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
