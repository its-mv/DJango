from django.urls import path, include
from .views import *
urlpatterns = [
    path('', item_list, name="list"),
    path('create/', create, name="create"),
    path('demo/', demo, name="demo"),
    
]
