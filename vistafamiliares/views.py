from django.http import HttpResponse
from django.template import loader
from vistafamiliares.models import Familia

def inicio(request):
    return HttpResponse('''<h1>MVT - Python Django</h1>
                        <h3>Lista de alumnos:</h3>
                        <li>Jonatan</li>
                        <li>Jonas</li>
                        <li>Jorge</li>
                        ''')

def pepe(request):
    template1 = loader.get_template('consigna.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def mi_familia(request):
    template1 = loader.get_template('familiares.html')
    nombre=""
    edad=0
        
    familia = Familia(nombre='Juan',edad=26)
    # familia.save()
    # lista_familia = familia.objects.all()
    # render1=template1.render({'Nombre': nombre, 'Edad': edad})
    render1=template1.render({'Nombre': familia})
    
    return HttpResponse(render1)