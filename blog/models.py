from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    p = models.TextChoices('p', 'Volunteer Donor')
    ptype = models.CharField(blank=True, choices=p.choices, max_length=10)
    
class Food_Bank(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=100)
    incharge = models.CharField(max_length=30)
    
class Status(models.Model):
    stu = models.TextChoices('s', 'Requested Accepted Collected Donated')
    description = models.CharField(blank=True, choices=stu.choices, max_length=20)
    
class Request(models.Model):
    did = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    food_item = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=100)
    rtime = models.DateTimeField(default= timezone.now)
    sid = models.ForeignKey(Status, on_delete=models.CASCADE)
    
class Reports(models.Model):
    rid = models.ForeignKey(Request, on_delete=models.CASCADE)
    vid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    human = models.PositiveSmallIntegerField()
    animal = models.PositiveSmallIntegerField()

class Onsite_Processing(models.Model):
    rid = models.ForeignKey(Request, on_delete=models.CASCADE)
    vid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    test = models.TextChoices('tests', 'pass fail')
    type_who = models.TextChoices('whom', 'humans animals')
    smell = models.CharField(blank=True, choices=test.choices, max_length=10)
    visual = models.CharField(blank=True, choices=test.choices, max_length=10)
    pickup_time = models.DateTimeField(default= timezone.now)
    result = models.CharField(blank=True, choices=type_who.choices, max_length=10)

class Donation_Process(models.Model):
    oid = models.ForeignKey(Onsite_Processing, on_delete=models.CASCADE)
    sid = models.ForeignKey(Status, on_delete=models.CASCADE)
    type_range = models.TextChoices('place', 'direct_donation food_bank')
    dtype = models.CharField(blank=True, choices=type_range.choices, max_length=20)
    location = models.CharField(max_length=100)
