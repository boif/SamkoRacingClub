from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=70, verbose_name='Name')
    image = models.ImageField(upload_to='images', verbose_name='Image')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Price', default = 0)

    objects = models.Manager()
    def __str__(self):
        return self.title