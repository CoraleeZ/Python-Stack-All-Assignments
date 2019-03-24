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
        if len(postData['pw']) < 8:
            errors["pw"] = "Password should be at least 8 characters"
        if postData['cpw']!=postData['pw']:
            errors['cpw']='Password does not match'
        return errors



class users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UsersManager() 

class authors(models.Model):
    author_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class books(models.Model):
    book_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(users,related_name='book')
    author=models.ForeignKey(authors,related_name='book')


class reviews(models.Model):
    review=models.TextField()
    rate=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    book=models.ForeignKey(books,related_name='review')
    user=models.ForeignKey(users,related_name='review')




# Create your models here.
