from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='subject'),
    path('topic/', views.index, name='topic'),
]