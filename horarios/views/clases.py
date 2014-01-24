from horarios.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from custom_decorators import *
from collections import namedtuple
import json
import pytz
from django.conf import settings
import datetime


def _json_object_hook(d): return namedtuple('object', d.keys())(*d.values())

def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

@json_response 
def get_clases_json(request):
    try:
        fecha = datetime.datetime.strptime(a, "%d/%m/%y").date()
        clases = Clase.objects.filter(fecha=fecha)
    except:
        cargos = ""
    json_data = []
    
    for cargo in cargos:
        json_data.append({
                'cargo_id': str(cargo.id),
                'taller': str(cargo.taller.nombre),
                'taller_id': str(cargo.id),
                'total': str(cargo.cantidad),
                'adeudo': str(cargo.adeudo()),
                'pagado': str(cargo.totalpagado)
            })
        
    return json_data

@json_response 
def update_clase_json(request):
    response = {}
    salones = json2obj(request.POST['clases'])
    try:
        fecha = datetime.datetime.strptime(request.POST['fecha'], "%d/%m/%y").date()
        hora = Horario.objects.get(hora=request.POST['hora'])
        grupo = Grupo.objects.get(nombre=request.POST['grupo'])
    except:
        return {'error':'error en los datos enviados'}
    
    clases_actuales = Clase.objects.filter(fecha=fecha,hora=hora,grupo=grupo)
    for clase in clases_actuales:
            clase.estatus = 'cancelada'
            clase.save()
            response[clase]='cancelada'
            
    for salon in salones:
        salon = Salon.objects.get(nombre=salon)
        try:
            clase = Clase.objects.get_or_create(fecha=fecha,salon=salon,grupo=grupo,hora=hora)[0]
            clase.estatus = 'activa'
            clase.save()
            response[clase]='activada'
        except:
            pass
    
#     for cargo in cargos:
#         json_data.append({
#                 'cargo_id': str(cargo.id),
#                 'taller': str(cargo.taller.nombre),
#                 'taller_id': str(cargo.id),
#                 'total': str(cargo.cantidad),
#                 'adeudo': str(cargo.adeudo()),
#                 'pagado': str(cargo.totalpagado)
#             })
#         
    return response
