from django.shortcuts import render
from AppCoder.models import Familia
from django.http import HttpResponse

def familiar(request):
    
    familia = Familia(nombre = "Maria", edad = 38, fecha = "1984-8-23") 
    familia.save()
    mostrar = f"Nombre del familiar:{familia.nombre}    Edad del familiar:{familia.edad}    Nacimiento del familiar: {familia.fecha}"
    return HttpResponse(mostrar)

def familiar_2(request):    
    
    familia_2 = Familia(nombre = "Miguel", edad = 40, fecha = "1982-4-16")
    mostrar_2 = f"Nombre del familiar:{familia_2.nombre}    Edad del familiar:{familia_2.edad}    Nacimiento del familiar: {familia_2.fecha}"
    return HttpResponse(mostrar_2)

def familiar_3(request):
    
    familia_3 = Familia(nombre = "Luana", edad = 25, fecha = "1997-2-28")
    mostrar_3 = f"Nombre del familiar:{familia_3.nombre}    Edad del familiar:{familia_3.edad}    Nacimiento del familiar: {familia_3.fecha}"
    return HttpResponse(mostrar_3)
    