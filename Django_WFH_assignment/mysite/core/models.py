from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    position = models.CharField(max_length=50)
    company_logo = models.CharField(max_length=250)
    background_img = models.CharField(default='https://www.scylladb.com/wp-content/uploads/Rumi-Group-scaled-1-1899x2048.jpg', max_length=250)
    bio = models.TextField()
    slug= AutoSlugField(populate_from='name', null=True , default=None)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email= models.EmailField()
    profile_picture = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.profile.name
    

class Schedule(models.Model):
    day = models.IntegerField()
    date = models.CharField(max_length=50)
    timing_1 = models.CharField(max_length=100)
    timing_2 = models.CharField(max_length=100)
    timing_3 = models.CharField(max_length=100)
    timing_4 = models.CharField(max_length=100)

    class Meta:
        ordering = ['day']
    
    