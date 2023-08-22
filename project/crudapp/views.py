from django.shortcuts import render
from .models import *
# Create your views here.
def item_list(request):
    items = Item.objects.all() # select * from Item.
    return render(request, 'list.html', {'items':items})