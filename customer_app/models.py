from django.db import models

from accounts.models import BaseModel, Room, User

# Create your models here.
class Dog(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True,blank=True)
    breed = models.CharField(max_length=200,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    temperament = models.CharField(max_length=200,null=True,blank=True)
    health_status = models.CharField(max_length=200,null=True,blank=True)
    photo = models.ImageField(upload_to='dog_photos/',null=True,blank=True)
    
class Boarding(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE,related_name='staff_boarding',null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    room_preference = models.ForeignKey(Room,on_delete=models.CASCADE,null=True,blank=True)
    special_requirements = models.TextField(null=True,blank=True)
    STATUS_CHOICES = [('upcoming', 'Upcoming'),('active', 'Active'),('completed', 'Completed'),]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')
    
class Feedback(BaseModel):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)

