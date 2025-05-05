from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_receptu, name='seznam_receptu'),
    path('recept/<int:id>/', views.detail_receptu, name='detail_receptu'),
]
