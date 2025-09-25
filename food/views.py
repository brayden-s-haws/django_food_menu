from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
# Create your views here.
def index(request):
    # Get items from the database
    item_list = Item.objects.all()
    # Creating context
    context = {
        "item_list": item_list
    }
    # Passing context to the template
    return  render(request, "food/index.html", context)

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        "item": item
    }
    return render(request, "food/detail.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("food:index")

    context = {
        "form": form
    }
    return render(request, "food/item_form.html", context)
def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    context = {
        "form": form
    }
    return render(request, "food/item_form.html", context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/delete_item.html")