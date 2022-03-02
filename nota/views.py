from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Nota

def get_nota(request, id_nota):
    try:
        nota = Nota.objects.get(pk=id_nota)
        return JsonResponse({ 'title': nota.title, 'body': nota.body }, status = 200)
    except Nota.DoesNotExist:
        return JsonResponse({ 'error' : 'Esa nota no existe' }, status = 400)
    except Exception as e:
        return JsonResponse({ 'error' : 'Ocurrio un error: ' + e }, status = 500)

def redefinir(nota):
    return {'title': nota.title, 'body': nota.body, 'id': nota.id}

def get_notas(request):
    try:
        notas = list(Nota.objects.all())
        notas = list(map(redefinir, notas))
        return JsonResponse({ 'notas': notas}, status = 200)
    except Exception as e:
        return JsonResponse({ 'error' : 'Ocurrio un error: ' + e }, status = 500)

def delete_nota(request, id_nota):
    try:
        nota = Nota.objects.get(pk=id_nota)
        print(nota.body, nota.title, nota.id)
        nota.delete()
        response = JsonResponse({'msj': 'funciona'}, status = 200)
    except Nota.DoesNotExist:
        response = JsonResponse({ 'error' : 'Esa nota no existe' }, status = 400)
    except Exception as e:
        response = JsonResponse({ 'error' : 'Ocurrio un error: ' + e }, status = 500)
    return response

def create_nota(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        nota = Nota.objects.create(title=body['title'], body=body['body'])
        return JsonResponse(redefinir(nota), status = 200)
    except Exception as e:
        response = JsonResponse({ 'error' : 'Ocurrio un error: ' + e }, status = 500)
    return response
