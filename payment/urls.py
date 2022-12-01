from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment/', views.BasketView, name='basket'),
]
