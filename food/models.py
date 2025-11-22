from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name + ":" + str(self.item_price)

    def get_absolute_url(self):
        return reverse('food:index')

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_image = models.URLField(max_length=500,default='https://images.unsplash.com/vector-1750272454955-229749cf8e08?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZvb2QlMjBpdGVtJTIwcGxhY2Vob2xkZXJ8ZW58MHx8MHx8fDA%3D')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    added_on = models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name