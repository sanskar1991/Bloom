from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import NetworkList, AddSubList, NewExposure
from .forms import NetListForm, AddSubListForm, NewExpForm

# Create your views here.
def index(request):
    """Home page"""
    return HttpResponse("<h1>Hello World!</h1>")

def add_sub_list(request):
    """AddSubnetList"""
    add_sub_list = AddSubList.objects.all()
    context = {'add_sub_list':add_sub_list}
    return render(request, 'add_sub_list.html', context)

def network_list(request):
    """AddSubnetList"""
    network_list = NetworkList.objects.all()
    context = {'network_list':network_list}
    return render(request, 'network_list.html', context)

def new_exposure(request):
    """NewExposure"""
    new_expo = NewExposure.objects.all()
    context = {'new_expo':new_expo}
    return render(request, 'new_expo.html', context)
    
    