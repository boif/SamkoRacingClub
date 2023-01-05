from django.db import models
from django.contrib.auth.models import User
    
class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=70, verbose_name='Name')
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='Description')
    image = models.ImageField(upload_to='images', verbose_name='Image')

    objects = models.Manager()
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='images/profile', default='images\profile\default.png', blank=True)
    vk = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)