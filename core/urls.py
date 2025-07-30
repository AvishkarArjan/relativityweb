from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nebula/', views.nebula, name='nebula'),
    path('voyager/', views.voyager, name='voyager'),

]



            
