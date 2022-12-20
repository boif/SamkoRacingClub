from django.db import models
from django.contrib.auth.models import User
    
class Image(models.Model):
    title = models.CharField(max_length=70, verbose_name='Name')
    image = models.ImageField(upload_to='images', verbose_name='Image')

    objects = models.Manager()
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/profile', default='images\profile\default.png', blank=True)
    vk = models.CharField(max_length=50, null=True, blank=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.user)