from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    # user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'is_staff':True})
    # user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Page(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=255)
    
class Like(Page):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, parent_link=True)
    likes = models.IntegerField()