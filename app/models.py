from abc import abstractclassmethod
from pydoc import describe
from random import choice
from weakref import proxy
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.html import format_html
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django import forms

# Create your models here.


SELECT_CUSTOMER_TYPE=(
     
     ('Individual (Persanol Goods)','Indivisual (Persanol Goods)'),
     ('Company (Industrial/Commercial Goods)','Company (Industrial/Commercial Goods)'),
     ('Transpoter','Transpoter'),
     ('Truck Owner','Truck Owner'),
 )

SELECT_GOOD_TYPE=((
    

))
   
   
    

TRUCK_TYPE=(    

('ACE / DOST / PICKUP (1.5 TON)','ACE / DOST / PICKUP (1.5 TON)'),
('TATA 407 / EICHER 14FT (4 TON)','TATA 407 / EICHER 14FT (4 TON)'),
('EICHER 17FT (5 TON)','EICHER 17FT (5 TON)'),
('EICHER 19FT (7 TON)','EICHER 19FT (7 TON)'),
('20FT CONTAINER (6.5 TON)','20FT CONTAINER (6.5 TON)'),
('TATA TRUCK (10 TON)','TATA TRUCK (10 TON)'),
('32FT CONTAINER (7 TON)','32FT CONTAINER (7 TON)'),
('32FT CONTAINER (14 TON)','32FT CONTAINER (14 TON)'),
('32 / 40 FEET OPEN TRAILER','32 / 40 FEET OPEN TRAILER'),
('SELECT TRUCK LATER','SELECT TRUCK LATER'),
('TAURUS (18 TON) N.A','TAURUS (18 TON) N.A'),
('PARCEL SERVIC','PARCEL SERVIC'),


)

   
#User Goods Selections

class Select_Goods(models.Model):
    pick_city=models.CharField(max_length=250)
    drop_city=models.CharField(max_length=250)
    truck_type=models.CharField(max_length=250 , choices=TRUCK_TYPE)
    Select_date_type = models.DateField()
    Select_good_type=models.CharField(max_length=230)
    Select_customer_type=models.CharField(max_length=250 , choices=SELECT_CUSTOMER_TYPE)
    enter_weight=models.CharField(max_length=3) 
    mobile=models.CharField(max_length=10)
    
    
    class Meta:
        verbose_name_plural='CUSTOMER DATA' 


    def __str__(self):
        return str(self.truck_type)

# STATE_CHOICES=(
#     ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
#     ('Andhra Pradesh','Andhra Pradesh'),
#     ('Assam','Assam'),
#     ('Bihar','Bihar'),
#     ('Chandigarh','Chandigarh'),
#     ('Chhattisgarh','Chhattisgarh'),
#     ('Goa','Goa'),
#     ('Utter Pradesh','Utter Pradesh'),
#     ('Himachal Pradesh','Himachal Pradesh'),
#     ('Jammu & kasmir','Jammu & kasmir'),
# )




# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
#     first_name=models.CharField(max_length=90)
#     last_name=models.CharField(max_length=90)
#     birthday = models.DateField(default=None)
#     city=models.CharField(max_length=90)
#     state=models.CharField(max_length=90 , choices=STATE_CHOICES)
#     address=models.CharField(max_length=250, default=None)
   
    
#     def __str__(self):
#         return str(self.first_name)

#     class Meta:
#         verbose_name_plural='PROFILE'



class Vender(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE,null=True, blank=True)
    first_name=models.CharField(blank=True ,max_length=90  )
    last_name=models.CharField(blank=True ,max_length=90 )
    email=models.EmailField(max_length=250)
    Company_name_or_shop_name=models.CharField(max_length=250)
    GST_Number=models.CharField(blank=True , max_length=250)

    


    def __str__(self):
        return str(self.first_name)


    
 
    
  
  

    
