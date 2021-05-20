from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_polls_index'),
    path('create', views.create_poll, name='create_poll'),
    path('delete/<int:id>', views.delete_poll, name='delete_poll'),
    path('statics/<int:id>', views.poll_statics, name='poll_statics')
]