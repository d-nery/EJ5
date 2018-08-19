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
    map_data = json.load(open(os.path.join(settings.BASE_DIR,'app/map_templ.json')))
    map_data['chart']['caption'] = 'Mapa Show 1'
    map_data['data'] = [{
        'id': estados['AL'],
        'value': 4,
    }, {
        'id': estados['AM'],
        'value': 6,
    }, {
        'id': estados['BA'],
        'value': 210,
    }, {
        'id': estados['CE'],
        'value': 5,
    }, {
        'id': estados['GO'],
        'value': 1,
    }, {
        'id': estados['MG'],
        'value': 5,
    }, {
        'id': estados['MS'],
        'value': 2,
    }, {
        'id': estados['MT'],
        'value': 1,
    }, {
        'id': estados['PA'],
        'value': 2,
    }, {
        'id': estados['PB'],
        'value': 1,
    }, {
        'id': estados['PE'],
        'value': 4,
    }, {
        'id': estados['PR'],
        'value': 1,
    }, {
        'id': estados['RJ'],
        'value': 8,
    }, {
        'id': estados['RS'],
        'value': 2,
    }, {
        'id': estados['SC'],
        'value': 35,
    }, {
        'id': estados['SP'],
        'value': 970,
    }]

    map_data['colorrange']['code'] = '#6baa01'
    map_data['colorrange']['color'] = [{
        'maxvalue': 500,
        'code': 'f8bd19',
    }, {
        'maxvalue': 1000,
        'code': 'e44a00',
    }]

    extra_map_data = [{
        'estado': 'SP',
        'data': json.load(open(os.path.join(settings.BASE_DIR,'app/chart_templ.json')))
    }, {
        'estado': 'BA',
        'data': json.load(open(os.path.join(settings.BASE_DIR,'app/chart_templ.json')))
    }, {
        'estado': 'AL',
        'data': json.load(open(os.path.join(settings.BASE_DIR,'app/chart_templ.json')))
    }]

    extra_map_data[0]['data']['chart']['caption'] = 'Sao Paulo'
    extra_map_data[0]['data']['data'] = [{
                'label': 'BA',
                'value': 2,
            }, {
                'label': 'CE',
                'value': 3
            }, {
                'label': 'GO',
                'value': 1
            }, {
                'label': 'MG',
                'value': 5
            }, {
                'label': 'MT',
                'value': 1
            }, {
                'label': 'PA',
                'value': 2
            }, {
                'label': 'PB',
                'value': 1
            }, {
                'label': 'PE',
                'value': 3
            }, {
                'label': 'PR',
                'value': 1
            }, {
                'label': 'RJ',
                'value': 8
            }, {
                'label': 'RS',
                'value': 2
            }, {
                'label': 'SP',
                'value': 949
            }]

    extra_map_data[1]['data']['chart']['caption'] = 'Bahia'
    extra_map_data[1]['data']['data'] = [{
                'label': 'AM',
                'value': 6,
            }, {
                'label': 'BA',
                'value': 208
            }, {
                'label': 'CE',
                'value': 2
            }, {
                'label': 'MS',
                'value': 2
            }, {
                'label': 'PE',
                'value': 1
            }, {
                'label': 'SC',
                'value': 35
            }, {
                'label': 'SP',
                'value': 20
            }]

    extra_map_data[2]['data']['chart']['caption'] = 'Alagoas'
    extra_map_data[2]['data']['data'] = [{
                'label': 'AL',
                'value': 4,
            }, {
                'label': 'SP',
                'value': 1
            }]

    maps.append({
        'name': 'map1',
        'data': map_data,
        'title': 'Mapa 1',
        'extra': extra_map_data
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
        'extra': []
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
        'extra': []
    })

    for m in maps:
        with open(os.path.join(settings.STATIC_ROOT, m['name'] + '.json'), 'w') as f:
            json.dump(m['data'], f)

        with open(os.path.join(settings.BASE_DIR, 'app/static/' + m['name'] + '.json'), 'w') as f:
            json.dump(m['data'], f)

        for e in m['extra']:
            with open(os.path.join(settings.STATIC_ROOT, m['name'] + '-' + e['estado'] + '.json'), 'w') as f:
                json.dump(e['data'], f)

            with open(os.path.join(settings.BASE_DIR, 'app/static/' + m['name'] + '-' + e['estado'] + '.json'), 'w') as f:
                json.dump(e['data'], f)

    return render(request, 'app/index.html', { 'maps': maps })
