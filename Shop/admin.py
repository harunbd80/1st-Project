from django.contrib import admin
from . models import product
# Register your models here.
@admin.register(product)

class productModelAdmin(admin.ModelAdmin):
    list_display=['id','title','mein_price','discount_price','discription','brand','cetagory','product_img']