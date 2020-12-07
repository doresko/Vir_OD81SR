from django.shortcuts import render
from .models import JPG, PNG
import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    jpgs = JPG.objects.order_by('id')
    pngs = PNG.objects.order_by('id')
    return render(request, 'pictures/index.html', {
        'jpgs': jpgs,
        'pngs': pngs
        })
