from django.http import Http404
from django.shortcuts import redirect, render
from .forms import *
from .models import Link, LinkIpList
from django.contrib.auth.models import User
from account.models import UserData
from django.db.models import F



def home_view(request):
    return render(request, 'index.html')


def ads_view(request, slug):
    linkuser = Link.objects.get(slug=slug).user

    linkownuser = User.objects.get(username=linkuser)

    linkuserid = Link.objects.get(slug=slug)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')

    useripstr = str(userip)

    iplist= LinkIpList.objects.filter(link__slug=slug)
    
    iplistaddr = list()

    for i in iplist:
        iplistaddr.append(i.ipaddr)


    linkclickupt = UserData.objects.filter(user=linkownuser).update(clicklink=F('clicklink') + 1)

    linkclick = UserData.objects.get(user=linkownuser).clicklink

    if useripstr not in iplistaddr:
        form = LinkIpList.objects.create(link=linkuserid, ipaddr=useripstr)
        linkclickupt = UserData.objects.filter(user=linkownuser).update(coins=F('coins') + 1)
    

    contex = {
        
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
