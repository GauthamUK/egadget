from django.urls import path
from.views import *

urlpatterns = [
    path('cust',CustomerHomeView.as_view(),name='custhome'),
    path('pdetail/<int:id>',ProductDetailView.as_view(),name='pdet'),
    path('acart/<int:id>',addcart,name='acart'),
    path('cartlist',CartListView.as_view(),name='clist'),
    path('rcart/<int:id>',removecart,name='rcart'),
    path('pay/<int:id>',PaymentView.as_view(),name='pay'),
    
    path('orders',OrderListView.as_view(),name='orders'),
    path('cancelorder/<int:id>',cancelorder,name='ocancel'),



    
]   