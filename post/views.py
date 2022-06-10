from django.http import Http404
from django.shortcuts import redirect, render
from .forms import *
from .models import Link, LinkIpList
from django.contrib.auth.models import User
from account.models import UserData
from django.db.models import F



def home_view(request):
    return render(request, 'index.html')


import requests
import json


def get(ip):
    endpoint = f'https://ipinfo.io/{ip}/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()

    return data['country']

def ads_view(request, slug):
    linkuser = Link.objects.get(slug=slug).user

    linkownuser = User.objects.get(username=linkuser)

    linkuserid = Link.objects.get(slug=slug)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = '5.197.211.8' # request.META.get('REMOTE_ADDR')

    useripstr = str(userip)



    iplist= LinkIpList.objects.filter(link__slug=slug)
    
    iplistaddr = list()

    my_country = get(useripstr)

    

    for i in iplist:
        iplistaddr.append(i.ipaddr)


    linkclickupt = UserData.objects.filter(user=linkownuser).update(clicklink=F('clicklink') + 1)

    linkclick = UserData.objects.get(user=linkownuser).clicklink

    if useripstr not in iplistaddr and my_country == 'AZ':
        form = LinkIpList.objects.create(link=linkuserid, ipaddr=useripstr)
        linkcoinsupt = UserData.objects.filter(user=linkownuser).update(coins=F('coins') + 1)
    

    contex = {
        'link' : linkuserid,
    }


    return render(request, 'ads.html', contex)

def create_link(request):
    form = LinkForm()

      



    if request.method == 'POST':
        form = LinkForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user 
            post.save()
            return redirect('home')
        else:
            form = LinkForm()
    contex = {
        'form': form,
    }

    return render(request, 'link-add.html', contex)


# Create your views here.
