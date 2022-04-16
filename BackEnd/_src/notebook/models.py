from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20,blank = False, null = True)
    name =  models.CharField(max_length=20,blank = False, null = True)
    last =  models.CharField(max_length=20,blank = False, null = True)
    email =   models.EmailField(blank=False)
    time = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self): # Python 2
        return self.username

    def __str__(self): # Python 3
        return self.username

    