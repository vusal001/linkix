from django.http import Http404
from django.shortcuts import render
from .forms import *

def home_view(request):
    return render(request, 'index.html')


def create_link(request):
    form = LinkForm()

    if request.method == 'POST':
        form = LinkForm(request.POST or None)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user 
            form.save()


    contex = {
        'form': form,
    }

    return render(request, 'index.html', contex)


# Create your views here.
