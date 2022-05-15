from django.shortcuts import render
from .forms import *


def create_link(request):
    form = LinkForm()

    if request.method == 'POST':
        form = LinkForm(request.POST or None)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user 
            form.save()


    contex =[
        'form': form,
    ]

    return render(request, 'linkadd.html', contex)


# Create your views here.
