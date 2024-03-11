from django.contrib import admin
from django.urls import path
from  app1 import views
app_name="app1"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
]
