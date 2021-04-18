from django.urls import path
from . import views


urlpatterns = [

    path('', views.UrlDetails,name='Form'),
    path('Search.html', views.Search,name='Search'),
    path('GetImages.html',views.getimage,name='Getimage')

]