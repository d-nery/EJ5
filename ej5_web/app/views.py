import json
import os

from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.conf import settings

estados = {
    'AC': '001', 'AL': '002', 'AP': '003', 'AM': '004',
    'BA': '005', 'CE': '006', 'DF': '007', 'ES': '008',
    'GO': '009', 'MA': '010', 'MT': '011', 'MS': '012',
    'MG': '013', 'PA': '014', 'PB': '015', 'PR': '016',
    'PE': '017', 'PI': '018', 'RJ': '019', 'RN': '020',
    'RS': '021', 'RO': '022', 'RR': '023', 'SC': '024',
    'SP': '025', 'SE': '026', 'TO': '027',
}

def index(request):
    maps = []

    # Update jsons
    maps.append({
        'name': 'map1',
        'title': 'Divergências',
    })

    maps.append({
        'name': 'map2',
        'title': 'Disparidades',
    })

    return render(request, 'app/index.html', { 'maps': maps })

def disparities(request, id):
    table = {
        "datajson": "http://127.0.0.1:5000/tabela" + str(id)
        "headers": [
            'CIB', 'UF', 'NUM_DOCFIS', 'COD_CFO_aquis', 'COD_CFO_rastr',
            'COD_ESTAB_aquis', 'COD_ESTAB_rastr', 'COD_PRODUTO_aquis',
            'COD_PRODUTO_rastr', 'DAT_OPER_aquis', 'DAT_OPER_rastr',
            'VLR_CRED_DIF_ALIQ_aquis', 'VLR_CRED_DIF_ALIQ_rastr',
            'VLR_CRED_ICMS_aquis', 'VLR_CRED_ICMS_rastr',
            'VLR_ICMSS_aquis', 'VLR_ICMSS_rastr'
        ]
    }

    return render(request, 'app/table.html', { 't': table })
