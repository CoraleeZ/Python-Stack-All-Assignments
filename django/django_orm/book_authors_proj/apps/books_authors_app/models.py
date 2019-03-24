from django.db import models

class books(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class authors(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    book=models.ManyToManyField(books,related_name='author')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    notes=models.TextField()


# Create your models here.
