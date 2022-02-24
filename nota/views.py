from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Nota

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_nota(request, id_nota):
    try:
        nota = Nota.objects.get(pk=id_nota)
        return JsonResponse({ 'title': nota.title, 'body': nota.body }, status = 200)
    except Nota.DoesNotExist:
        return JsonResponse({ 'error' : 'Esa nota no existe' }, status = 400)
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
