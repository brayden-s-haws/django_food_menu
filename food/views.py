from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone


# Create your views here.

logger = logging.getLogger(__name__)

# @login_required
# @cache_page(60 * 15)
# @vary_on_headers('User-Agent')
def index(request):
    # Get items from the database
    logger.info("Fetching items from the database")
    logger.info(f"User [{timezone.now().isoformat()}] {request.user} requested the item list from {request.META.get('REMOTE_ADDR')}")
    item_list = Item.objects.all()
    logger.debug(f'Fetched {item_list.count()} items from the database')
    # print(item_list)
    paginator = Paginator(item_list, 5)
    # print('Paginator:' ,paginator)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Creating context
    context = {
        "page_obj": page_obj
    }
    # Passing context to the template
    return  render(request, "food/index.html", context)

class FoodDirectoryView(ListView):
    model = Item
    template_name = 'food/index.html'

def detail(request, id):
    logger.info(f"Fetching item with id: {id} from the database")
    try:
        item = get_object_or_404(Item, pk=id)
        # item = Item.objects.get(id=id)
        logger.debug(f"Item found: {item.item_name} (${item.item_price})")
    except Exception as e:
        logger.error("Error fetching the item %s: %s ",id, e)
        raise
    context = {
        "item": item
    }
    return render(request, "food/detail.html", context)

# class FoodDetailView(DetailView):
#     model = Item
#     template_name = 'food/detail.html'
#     context_object_name = 'item'

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

def get_objects(request):
    for item in Item.objects.all():
        print(item.item_name)

def get_objects_optimized(request):
    items = Item.objects.only('item_name')
    for item in items:
        print(item.item_name)