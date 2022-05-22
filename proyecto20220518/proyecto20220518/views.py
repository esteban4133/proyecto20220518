from multiprocessing import context
from re import template
from xml.dom.minidom import Document
import django
from django.http import HttpResponse
from django.template import Context, Template, loader



def saludo (request):
    return HttpResponse ("Hola mundo")


def saludo2(request):
    return HttpResponse(f"<h1>HOLA MUNDO <h1>")

def anotador (request, nombre1):
    plantilla=loader.get_template("templet1.html")
    documento = plantilla.render({"an":nombre1})
    return HttpResponse(documento)


def probando_temple (request):

    plantilla=loader.get_template("templet1.html")
    documento=plantilla.render({"nombre":"esteban"})
    return HttpResponse(documento)


   # mi_html= open(r"D:\Sincronizacion_Google\Python\VisualStudio\proyecto20220518\proyecto20220518\proyecto20220518\plantillas\templet1.html")
   # plantilla = Template(mi_html.read())
   # mi_html.close()
   # mi_contecto = Context()
   # documento = plantilla.render(mi_contecto)
   # return HttpResponse (documento)




