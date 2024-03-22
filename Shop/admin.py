from django.contrib import admin
from . models import product,customer
# Register your models here.
@admin.register(product)

class productModelAdmin(admin.ModelAdmin):
    list_display=['id','title','mein_price','discount_price','discription','brand','cetagory','product_img']

@admin.register(customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'name', 'division','district','thana','vllorroad','zipcode']