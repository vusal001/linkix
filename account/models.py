from statistics import mode
from xml.dom import UserDataHandler
from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    clicklink = models.IntegerField(verbose_name='Linkə keçid(lər)')
    coins = models.IntegerField(verbose_name='Coins')


    def __str__(self):
        return str(self.user)


class Userlinkips(models.Model):
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)

    ipaddr = models.CharField(verbose_name='Ip Adres', max_length=15)

    def __str__(self):
        return str(self.userdata)


# Create your models here.
