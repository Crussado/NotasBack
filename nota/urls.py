from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_nota>/get/', views.get_nota, name='get'),
    path('<int:id_nota>/delete/', views.delete_nota, name='delete')
]
