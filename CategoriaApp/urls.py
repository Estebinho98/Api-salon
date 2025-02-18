from django.urls import path
from .views import CategoriaView, SingleCategoryView

urlpatterns = [
    path('categories', CategoriaView.as_view(), name='Categories'),
    path('categories/<int:pk>', SingleCategoryView.as_view(), name='Detail-Categoriy'),


]