from django.http import HttpResponse
from django.template import loader

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

def familia(request):
    template1 = loader.get_template('familiares.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')