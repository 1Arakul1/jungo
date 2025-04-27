from django.urls import path
from . import views
from .views import (
    AddDogToProfileView,
    IndexView,
    BreedsView,
    DogsListView,  # Make sure DogsListView is imported
    DogCreateView,
    DogUpdateView,
    DogDeleteView,
    DogReadView,
    RemoveDogFromProfileView
)

app_name = 'dogs'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('breeds/', BreedsView.as_view(), name='breeds'),
    path('dogs/', DogsListView.as_view(), name='dogs_list'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/<int:pk>/', DogReadView.as_view(), name='dog_read'),
    path('dogs/<int:pk>/update/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete'),
    path('dogs/<int:dog_id>/add_to_profile/', AddDogToProfileView.as_view(), name='add_to_profile'),
    path('dogs/<int:dog_id>/remove_from_profile/', RemoveDogFromProfileView.as_view(), name='remove_dog_from_profile'),
]