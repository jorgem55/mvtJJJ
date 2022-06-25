from datetime import datetime
from multiprocessing import context
from unittest import loader
from django.http import HttpResponse
from django.template import Template
from django.template import Context

def inicio(request):
    return HttpResponse('<h1>MVT</h1>')

def pepe(request):
    template1 = loader.get_template('home.html')
    render1=template1.render({'nombre':'Momia','edad':4598})
    # archivo = open(r'D:\Curso Python 2022\31085\mvt_JFJMJZ\templates\home.html') #v1
    # template1= Template(archivo.read())#v1
    # archivo.close()#v1
    
    # context1= Context() #v1
    # render1=template1.render(context1) #v1
    
    return HttpResponse(f'Mi template: {render1}')