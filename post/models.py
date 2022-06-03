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
    slug = models.SlugField(verbose_name='Post slug', blank=True, null=True, unique=True)
    LINKTYPE=(
        ('Youtube videosu', 'Youtube videosu'),
        ('TikTok', 'TikTok'),
        ('Instagram', 'Instagram'),
        ('18+ kontent', '18+ kontent'),
        ('Oyun', 'Oyun'),
        ('Yükləmə linki', 'Yükləmə linki'),
        ('Film/Serial', 'Film/Serial'),
        ('Digər', 'Digər')
    )

    linktype = models.CharField(max_length=100, choices=LINKTYPE, verbose_name='Linkin kategoriyası')



    def save(self,  *args, **kwargs):
        while True:
            letters = string.ascii_letters + string.digits
            newslug = ''.join(random.choice(letters) for i in range(7))
            links = Link.objects.all().values_list('slug', flat=True)
            if newslug not in links:
                print(links)
                self.slug = newslug
                super().save(*args, **kwargs)
                break


    def __str__(self):
        return str(self.name)
# Create your models here.
