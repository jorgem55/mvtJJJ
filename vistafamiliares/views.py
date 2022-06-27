import random
from django.http import HttpResponse
from django.template import loader
from vistafamiliares.models import Familia

def inicio(request):
    template1 = loader.get_template('inicio.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def consigna(request):
    template1 = loader.get_template('consigna.html')
    render1=template1.render()
    return HttpResponse(f'{render1}')

def mi_familia(request):
    template1 = loader.get_template('familiares.html')
    
    db_familia = Familia.objects.all()
    render1=template1.render({'lista_familia': db_familia})
    
    return HttpResponse(render1)

def agregar_familiar(request):
    
    int=random.randrange(4)
    if int == 0:
        familia = Familia(nombre='Juan',edad=26,fecha_nacimiento='1996-08-11')
        familia.save()
    elif int == 1:
        familia = Familia(nombre='Cecilia',edad=20,fecha_nacimiento='2002-12-21')
        familia.save()
    elif int == 2:
        familia = Familia(nombre='Lorena',edad=35,fecha_nacimiento='1986-08-10')
        familia.save()
    else:
        familia = Familia(nombre='Mario',edad=56,fecha_nacimiento='1966-02-06')
        familia.save()
    
    return HttpResponse('<h3>Se agregó familiar a la DB</h3>')