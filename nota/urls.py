from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_nota>/get_nota/', views.get_nota, name='get_nota'),
    path('<int:id_nota>/delete_nota/', views.delete_nota, name='delete_nota'),
    path('get_notas/', views.get_notas, name='get_notas'),
    path('create_nota/', views.create_nota, name='create_nota')
]
