from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from food.managers import ItemManager


# Create your models here.
class Item(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user_name','item_price']),
        ]
    def __str__(self):
        return self.item_name + ":" + str(self.item_price)

    def get_absolute_url(self):
        return reverse('food:index')

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200,db_index=True)
    item_desc = models.CharField()
    item_price = models.DecimalField(max_digits=6,decimal_places=2,db_index=True)
    item_image = models.URLField(max_length=500,default='https://images.unsplash.com/vector-1750272454955-229749cf8e08?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZvb2QlMjBpdGVtJTIwcGxhY2Vob2xkZXJ8ZW58MHx8MHx8fDA%3D')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False) # soft delete flag
    deleted_at = models.DateTimeField(blank=True, null=True) # saves timestamp of deletion

    objects = ItemManager()
    all_objects = models.Manager()

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    added_on = models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name