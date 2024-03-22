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
    
#CUSTOMER PROFILE VIEW
DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)

class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField( max_length=200)
    division=models.CharField(choices=DIVISION_CHOICES, max_length=50)
    district=models.CharField( max_length=50)
    thana=models.CharField( max_length=50)
    vllorroad=models.CharField( max_length=50)
    zipcode=models.IntegerField()

    def __str__(self):
        return str(self.id)
    
