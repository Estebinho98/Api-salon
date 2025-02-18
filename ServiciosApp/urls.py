from django.urls import path
from .views import ServiciesView

urlpatterns = [
    path('servicies', ServiciesView.as_view({'get':'list'}), name='Servicies'),
    path('servicies/<int:pk>', ServiciesView.as_view({'get':'retrieve'}), name='Detail-Servicie'),

]