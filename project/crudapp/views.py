from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def item_list(request):
    items = Item.objects.all() # select * from Item.
    return render(request, 'list.html', {'items':items})
def create(request):
    if request.method == "POST":
        data = request.POST['item']
        des = request.POST['des']
        obj = Item(item=data, des=des)
        obj.save()
        return redirect('list')
    return render(request,'create.html')

def demo(request):
    name = "Dhoni"
    no = 7
    
    List = [1,2,3,4,5]
    return render(request, 'demo.html', {"Mahi":name, "No":no, "Array": List})