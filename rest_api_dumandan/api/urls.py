from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarListCreate.as_view(), name='car-view-create'),
    path('cars/<int:pk>/', views.CarRetrieveUpdateDestroy.as_view(), name='car-retrieve-update-destroy')
]   

