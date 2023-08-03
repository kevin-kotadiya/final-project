from django.db import models

# Create your models here.

class user(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class noted(models.Model):
    query = models.CharField(max_length=20)
    option = models.CharField(max_length=20)
    file = models.FileField(upload_to='notesFiles')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class feedback(models.Model):
     name = models.CharField(max_length=20)
     email = models.EmailField()
     number = models.BigIntegerField()
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)