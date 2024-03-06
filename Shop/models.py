from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CETAGORY_LIST=[
    ('P','Pent'),
    ('s','saree'),
    ('k','Lehanga'),
    ('j','Jersy'),
    ('sh','Shirt'),
]
BRAND_LIST=[
    ('a','Arong'),
    ('e','Easy'),
    ('z','Zara Man'),
    ('s','Sara'),
    ('b','Black Brids'),
]
class product(models.Model):
    title=models.CharField( max_length=50)
    mein_price=models.FloatField()
    discount_price=models.FloatField()
    discription=models.TextField()
    brand=models.CharField(choices=BRAND_LIST,max_length=2)
    cetagory=models.CharField(choices=CETAGORY_LIST,max_length=2)
    product_img=models.ImageField( upload_to='productimg', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str (self.id)
    
