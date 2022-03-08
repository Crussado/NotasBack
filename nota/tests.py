from django.test import TestCase, Client
from django.contrib.auth.models import User
import json

from nota.models import Nota
# Create your tests here.

class NotaApiCreateTest(TestCase):
    fixtures = ['nota.json']

    def setup(self):
        self.user = User.objects.create_user(username='test', password='test123', is_superuser=True)
        self.client = Client(HTTP_POST='localhost')
        self.client.login(username='test', password='test123')

    def test_crear_nota_success(self):
        cant_notas = Nota.objects.all().count()
        data = {'body': 'cuerpo', 'title': 'titulo'}
        response = self.client.post('/nota/create_nota/', data=json.dumps(data), content_type='application/json')

        assert response.status_code == 200
        assert Nota.objects.all().count() == cant_notas + 1
        nota_creada = Nota.objects.last()
        assert nota_creada.title == data['title']
        assert nota_creada.body == data['body']  

    def test_crear_nota_sin_key_body_failed(self):
        cant_notas = Nota.objects.all().count()
        data = {'title': 'titulo'}

        response = self.client.post('/nota/create_nota/', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert Nota.objects.all().count() == cant_notas 

    def test_crear_nota_sin_key_title_failed(self):
        cant_notas = Nota.objects.all().count()
        data = {'body': 'body'}

        response = self.client.post('/nota/create_nota/', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert Nota.objects.all().count() == cant_notas 

    def test_crear_nota_sin_title_failed(self):
        cant_notas = Nota.objects.all().count()
        data = {'title': '', 'body': 'body'}

        response = self.client.post('/nota/create_nota/', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert Nota.objects.all().count() == cant_notas 
        
    def test_crear_nota_sin_body_success(self):
        cant_notas = Nota.objects.all().count()
        data = {'title': 'titulo', 'body': ''}

        response = self.client.post('/nota/create_nota/', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 200
        assert Nota.objects.all().count() == cant_notas + 1
        nota_creada = Nota.objects.last()
        assert nota_creada.title == data['title']
        assert nota_creada.body == data['body']


class NotaApiDeleteTest(TestCase):
    fixtures = ['nota.json']

    def setup(self):
        self.user = User.objects.create_user(username='test', password='test123', is_superuser=True)
        self.client = Client(HTTP_POST='localhost')
        self.client.login(username='test', password='test123')

    def test_delete_success(self):
        cant_notas = Nota.objects.all().count()
        response = self.client.delete('/nota/3/delete_nota/')
        assert response.status_code == 200
        assert Nota.objects.all().count() == cant_notas - 1
        response = self.client.get('/nota/3/get_nota/')
        assert response.status_code == 400

    def test_delete_failed(self):
        cant_notas = Nota.objects.all().count()
        response = self.client.delete('/nota/0/delete_nota/')
        assert response.status_code == 400
        assert Nota.objects.all().count() == cant_notas 

        nota = Nota.objects.last().id + 1 
        response = self.client.delete('/nota/{0}/delete_nota/'.format(nota))
        assert response.status_code == 400
        assert Nota.objects.all().count() == cant_notas

class NotaApiGetNotasTest(TestCase):
    fixtures = ['nota.json']

    def setup(self):
        self.user = User.objects.create_user(username='test', password='test123', is_superuser=True)
        self.client = Client(HTTP_POST='localhost')
        self.client.login(username='test', password='test123')

    def test_get_notas_success(self):
        cant_notas = Nota.objects.all().count()
        response = self.client.delete('/nota/get_notas/')
        cant_notas_devueltas = len(response.json()['notas'])
        assert response.status_code == 200
        assert cant_notas == cant_notas_devueltas
