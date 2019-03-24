from __future__ import unicode_literals
from django.db import models
from datetime import datetime


#regex validation
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
      
        # add keys and values to errors dictionary for each invalid field
        if len(postData['ti']) < 2:
            errors["ti"] = "Title should be at least 2 characters"
        if shows.objects.filter(title=postData['ti']):
            errors['ti']="Title already exist"

        if len(postData['net']) < 3:
            errors["net"] = "Network name should be at least 3 characters"
        #str transform into datetime
        value = postData['d']
        if datetime.now()<datetime.strptime(value, '%m/%d/%Y'):
            errors['d']="Release date should not be late than today"
        if len(postData['des']) < 10 and len(postData['des']) > 0:
            errors["des"] = "Description should be at least 10 characters"
        return errors



class networks(models.Model):
    network_name=models.CharField(max_length=255)


class shows(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.CharField(max_length=255)
    desc=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    network=models.ForeignKey( networks ,related_name='show')
    objects = ShowsManager() 


    


    
# Create your models here.
