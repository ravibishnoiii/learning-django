from django.urls import path
from .import views

urlpatterns = [
    path('', views.all, name='all_home'),

]
 