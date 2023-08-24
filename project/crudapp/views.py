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



def delete(request, id):
    data = Item.objects.get(id=id)
    print(data)
    if request.method == "POST":
        data.delete()
        return redirect('list')
    elif request.method == "GET":
        return render(request,'delete.html', {'data':data})
    
    
def update(request, id):
    data = Item.objects.get(id=id)
    if request.method == "POST":
        data.item = request.POST['item']
        data.des = request.POST['des']
        data.save()
        return redirect('list')
    return render(request, 'update.html', {'data':data})
    


