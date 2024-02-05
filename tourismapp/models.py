from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Travel(models.Model):
    t_id=models.IntegerField(primary_key=True) 
    image=models.ImageField(upload_to="img") 
    place_name=models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
 
class Book(models.Model): 
    t_id=models.ForeignKey(Travel,on_delete=models.CASCADE)
    no_people=models.PositiveIntegerField(default=0)
    dates=models.DateField(null=True, blank=True)
    userid = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    price= models.IntegerField(default=0)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    t_id = models.ForeignKey(Travel, on_delete=models.CASCADE)
    no_people = models.PositiveIntegerField(default=0)
    dates=models.DateField(null=True, blank=True)

 




  
 


    



    
