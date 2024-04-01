from django.urls import path
from . import views


urlpatterns = [

    path('',views.AnimalListView.as_view(), name='animal_list'),
    path('<int:pk>',views.AnimalView.as_view(), name='animal_view'),
    path('add',views.AddAnimalView.as_view(), name='add_animal'),
    path('delete/<int:pk>',views.DeleteAnimalView.as_view(), name='delete_animal')
]