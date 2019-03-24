from __future__ import unicode_literals
from django.db import models
from datetime import datetime,timedelta
import re

email_regex=re.compile(r'^[a-zA-Z0_9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# name_regex=re.compile(r'^[a-zA-Z]')
# pw_regex=re.compile('\d.*[A-Z]|[A-Z].*\d')

#regex validation
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
      
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fn']) < 2:
            errors["fn"] = "First name should be at least 2 characters"
        if len(postData['ln']) < 2:
            errors["ln"] = "Last name should be at least 2 characters"
        if not email_regex.match(postData['em']):
            errors['em']='Email is not valid'
        if users.objects.filter(email=postData['em']):
            errors['em']='This email address already existed'
        #str transform into datetime
        if postData['birth']:
            if datetime.now()<datetime.strptime(postData['birth'], '%m/%d/%Y'):
                errors['birth']="Birthday should not be late than today"
            
            a=datetime.strptime('1/1/2013', '%m/%d/%Y')-datetime.strptime('1/1/2000', '%m/%d/%Y')
            if datetime.now()-datetime.strptime(postData['birth'], '%m/%d/%Y')<a:
                errors['birth']="User should at least be 13 years old"
        else:
            errors['birth']='please enter a date'
        if len(postData['pw']) < 8:
            errors["pw"] = "Password should be at least 8 characters"
        if postData['cpw']!=postData['pw']:
            errors['cpw']='Password does not match'
        return errors



class users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    birthday=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UsersManager() 

# Create your models here.
