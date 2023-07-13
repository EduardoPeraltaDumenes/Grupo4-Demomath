from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('demos1', views.demo1_view, name='demo1'),
    path('dem1',views.dem1,name="demos1"),
    path('demo2/', views.demo2_view, name='demo2'),
    path('demo3/', views.demo3_view, name='demo3'),
]
