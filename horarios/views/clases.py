from horarios.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from custom_decorators import *
import json
import pytz
from django.conf import settings

@json_response 
def list_cargos_usuario_json(request, usuarioID):
    try:
        cargos = Cargo.objects.filter(usuario__id=usuarioID)
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