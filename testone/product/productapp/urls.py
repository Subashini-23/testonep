from django.urls import path
from productapp import views
from django.urls import path
from . import views


urlpatterns = [
    # Product CRUD
    path('product/', views.create_product, name='create_product'),
    path('product/<str:prodId>/', views.get_product, name='get_product'),
    path('product/update/<str:prodId>/', views.update_product, name='update_product'),
    path('product/delete/<str:prodId>/', views.delete_product, name='delete_product'),

    # Order CRUD (add similar routes for OrderCreation)
    path('order/', views.create_order, name='create_order'),
    path('order/<str:orderId>/', views.get_order, name='get_order'),
    path('order/update/<str:orderId>/', views.update_order, name='update_order'),
    path('order/delete/<str:orderId>/', views.delete_order, name='delete_order'),
    


  


]