from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api"),
    path('order-list/',views.orderlist, name="order-list"),
    path('order-detail/<str:pk>',views.orderDetail, name="order-detail"),
    path('order-create/',views.orderCreate, name="order-create"),
    path('order-delete/<str:pk>',views.orderDelete, name="order-delete"),
    # path('menu-list/',views.menulist,name="menu-list"),
    # path()
    path('main_menu_list/',views.main_menu_list,name="main_menu_list"),
    path('main_menu_detail/<str:pk>',views.main_menu_detail,name="main_menu_detail"),
    path('main_menu_create/',views.main_menu_create,name="main_menu_create"),
    path('main_menu_delete/<str:pk>',views.main_menu_delete,name="main_menu_delete"),
    
]
