from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.
def index(request):
    # Get items from the database
    item_list = Item.objects.all()
    # Creating context
    context = {
        "item_list": item_list
    }
    # Passing context to the template
    return  render(request, "DjangoCourseMenuApp/index.html",context)

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        "item": item
    }
    return render(request, "DjangoCourseMenuApp/detail.html",context)

def item(request):
    return  HttpResponse("<h1>This is an item view</h1>")