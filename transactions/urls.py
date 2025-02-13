from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('transactions/', views.transaction_list, name='transaction_list'),
]