from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty),
    path('<str:char1>/<str:char2>/', views.my_novel, name='my_novel_kh'),
]
