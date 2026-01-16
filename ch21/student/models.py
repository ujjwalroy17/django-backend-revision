from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)
    
    # def __str__(self):
    #     return self.name
    
    # def __str__(self):
    #     return str(self.roll)
    
    
class Result(models.Model):
    subject = models.CharField(max_length=70)
    roll = models.IntegerField()
    marks = models.IntegerField()
    
    # def __str__(self):
    #     return self.subject
    

