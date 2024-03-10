from django.urls import path
from cart import views
app_name="cart"
urlpatterns = [
    path('addtocart/<n>',views.addtocart,name="addtocart"),
    path('cartview',views.cartview,name="cartview"),
    path('cart_remove/<n>',views.cart_remove,name="cart_remove"),
    path('cart_delete/<n>',views.cart_delete,name="cart_delete"),
    path('orderform',views.orderform,name="orderform"),
    path('orderview',views.orderview,name="orderview"),


    ]
