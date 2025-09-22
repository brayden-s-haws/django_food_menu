from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item,name='item'),
    path('<int:id>/',views.detail,name='detail'),
    ]