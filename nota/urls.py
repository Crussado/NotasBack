from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_nota>/get/', views.get_nota, name='get'),
    path('<int:id_nota>/delete/', views.delete_nota, name='delete'),
    path('dev_nota/', views.get_notas, name='devoler'),
    path('create_nota/', views.create_nota, name='create')
]
