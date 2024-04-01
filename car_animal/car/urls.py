from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='AllCars'),
    path('<int:pk>', views.CarView.as_view(), name='AllCars'),
    path('add', views.AddCarView.as_view(), name='AddCar'),
    path('delete/<int:pk>', views.DeleteCarView.as_view(), name='DeleteCar')
]