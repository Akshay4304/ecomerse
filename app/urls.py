from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('store/',store,name='store'),
    path('store/<slug:category_slug>/',store,name='products_by_category'),
    path('store/<str:slug>/<int:id>/',product_details,name='product_details'),
   
]