from django.urls import path
from shop import views
app_name="shop"
urlpatterns = [
    path('',views.allcategories,name="allcat"),
    path('allprod/<p>',views.allproducts,name="allprod"),
    path('detail/<c>',views.alldetails,name="detail"),
    path('register',views.register,name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),



]