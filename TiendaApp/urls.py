from django.urls import path
from .views import BuyView, SingleBuyView

urlpatterns = [
    path('buy', BuyView.as_view(), name='BUY'),
    path('buy/<int:pk>', SingleBuyView.as_view(), name='Detail-Buy'),
]