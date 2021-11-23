from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    # instead of ls.name in name, 
    # # we can setup all vars ahead
    # my_dict = {}
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {
        "name":ls.name,
        "ls": ls
    })
    #item = ls.item_set.get(id=1)
    # original
    #ls = ToDoList.objects.get(name=name)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
    #return HttpResponse("<h1>%s</h1> %ls.name")

def home(response):
    return render(response, "main/home.html", {
    })