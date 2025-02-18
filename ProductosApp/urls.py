from django.urls import path, include
from .views import ProductsView, SingleProductView

urlpatterns = [
    path('products', ProductsView.as_view()),
    path('products/<int:pk>', SingleProductView.as_view()),

]