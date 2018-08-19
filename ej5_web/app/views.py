import json
import os

from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.conf import settings

def index(request):
    maps = []

    # Update jsons
    map_data = json.load(open(os.path.join(settings.BASE_DIR,'app/map_templ.json')))
    map_data['chart']['caption'] = 'Mapa Show 1'
    map_data['data'] = []

    for i in range(1,28):
        map_data['data'].append({
            'id': '{:03d}'.format(i),
            'value': i/10,
        })

    maps.append({
        'name': 'map1',
        'data': map_data,
        'title': 'Mapa 1',
    })

    map_data = json.load(open(os.path.join(settings.BASE_DIR,'app/map_templ.json')))
    map_data['chart']['caption'] = 'Mapa Show 2'
    map_data['data'].extend([{
        'id': '001',
        'value': 0.1,
    }, {
        'id': '002',
        'value': 0.2,
    }, {
        'id': '003',
        'value': 0.3,
    }])

    maps.append({
        'name': 'map2',
        'title': 'Mapa 2',
        'data': map_data,
    })

    map_data = json.load(open(os.path.join(settings.BASE_DIR,'app/map_templ.json')))
    map_data['chart']['caption'] = 'Mapa Show 3'
    map_data['data'].extend([{
        'id': '001',
        'value': 0.1,
    }, {
        'id': '002',
        'value': 0.2,
    }, {
        'id': '003',
        'value': 0.3,
    }, {
        'id': '004',
        'value': 0.4,
    }])

    maps.append({
        'name': 'map3',
        'title': 'Mapa 3',
        'data': map_data,
    })

    for m in maps:
        with open(os.path.join(settings.STATIC_ROOT, m['name'] + '.json'), 'w') as f:
            json.dump(m['data'], f)

        with open(os.path.join(settings.BASE_DIR, 'app/static/' + m['name'] + '.json'), 'w') as f:
            json.dump(m['data'], f)

    return render(request, 'app/index.html', { 'maps': maps })
