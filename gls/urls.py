from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='main'),
   path('product/', views.product, name='catalog'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('add/', views.add, name='add_card'),
]