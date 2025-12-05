from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'food'
urlpatterns = [
    path('',cache_page(60*15)(views.index),name='index'),
    path('<int:pk>/',views.FoodDetailView.as_view(),name='detail'),
    path('add/',views.CreateItemView.as_view(),name='add'),
    path('update/<int:pk>/',views.UpdateItemView.as_view(),name='update_item'),
    path('delete/<int:pk>/',views.DeleteItemView.as_view(),name='delete_item'),
    ]