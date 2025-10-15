from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


# Create your views here.

# @login_required
# def index(request):
#     # Get items from the database
#     item_list = Item.objects.all()
#     # Creating context
#     context = {
#         "item_list": item_list
#     }
#     # Passing context to the template
#     return  render(request, "food/index.html", context)

class FoodDirectoryView(ListView):
    model = Item
    template_name = 'food/index.html'

# def detail(request, id):
#     item = Item.objects.get(id=id)
#     context = {
#         "item": item
#     }
#     return render(request, "food/detail.html", context)

class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.user_name = request.user
#             form.save()
#             return redirect("food:index")
#
#     context = {
#         "form": form
#     }
#     return render(request, "food/item_form.html", context)

class CreateItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item_form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)




# def update_item(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect("food:index")
#     context = {
#         "form": form
#     }
#     return render(request, "food/item_form.html", context)

class UpdateItemView(UpdateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user)

# def delete_item(request, id):
#     item = Item.objects.get(id=id)
#     if request.method == "POST":
#         item.delete()
#         return redirect("food:index")
#     return render(request, "food/delete_item.html")

class DeleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy('food:index')