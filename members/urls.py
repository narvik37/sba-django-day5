from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('git', views.git),
        path('test2', views.test2),
        path('signup', views.signup),
        path('gugu', views.gugu),

        ]
