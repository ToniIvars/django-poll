from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_polls_index'),
    path('create', views.create_poll, name='create_poll')
]