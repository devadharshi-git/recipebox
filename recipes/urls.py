from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_create, name='recipe_add'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
]
