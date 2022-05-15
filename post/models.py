from statistics import mode
from django.db import models
import random
import string


class Link(models.Model):
    name = models.CharField(verbose_name='Link adi(sherti)', max_length=100)
    link  =  models.URLField(verbose_name='Link')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Yerlesdirilme tarixi')
    active = models.BooleanField(default=False, verbose_name='Aktiv?')
    blok = models.BooleanField(default=False, verbose_name='Blok et')
    slug = models.SlugField(verbose_name='Post slug', blank=True, null=True)
    

    def save(self,  *args, **kwargs):
        
        letters = string.ascii_letters + string.digits
        self.slug = ''.join(random.choice(letters) for i in range(7))
        super().save(*args, **kwargs)


# Create your models here.
