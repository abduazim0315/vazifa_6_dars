from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('car/<int:car_id>/', views.car_detail),
]