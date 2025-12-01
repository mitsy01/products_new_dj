from django.urls import path
from . import views


urlpatterns = [
    path('', views.basket_detail, name='basket_detail'),
    path('add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', views.basket_del, name='basket_remove'),
    path('clear/', views.basket_clear, name='basket_clear'),
]
