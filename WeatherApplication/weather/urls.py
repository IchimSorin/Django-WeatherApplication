from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="weather"),   #the path for our index view
    path('del/<int:item_id>', views.remove, name="del"),
]