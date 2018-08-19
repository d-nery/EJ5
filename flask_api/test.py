from flask import Flask
from flask import jsonify
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

estados = {
    'AC': '001', 'AL': '002', 'AP': '003', 'AM': '004',
    'BA': '005', 'CE': '006', 'DF': '007', 'ES': '008',
    'GO': '009', 'MA': '010', 'MT': '011', 'MS': '012',
    'MG': '013', 'PA': '014', 'PB': '015', 'PR': '016',
    'PE': '017', 'PI': '018', 'RJ': '019', 'RN': '020',
    'RS': '021', 'RO': '022', 'RR': '023', 'SC': '024',
    'SP': '025', 'SE': '026', 'TO': '027',
}

mapa1_df = pd.read_csv('mapa1.csv')
mapa1_AL_df = pd.read_csv('map1AL.csv')
mapa1_BA_df = pd.read_csv('map1BA.csv')
mapa1_SP_df = pd.read_csv('map1SP.csv')

out = {
    "chart": {
        "caption": "Divergências",
        "subcaption": "Jun 2018",
        "includevalueinlabels": "1",
        "labelsepchar": ": ",
        "entityFillHoverColor": "#b5c23f",
        "theme": "fusion",
        "showLegend": "1"
    },
    "colorrange": {
        "minvalue": "0",
        "code": "#6baa01",
        "gradient": "1",
        "color": [{
            "maxvalue": 500,
            "code": "f8bd19"
        }, {
            "maxvalue": 1000,
            "code": "e44a00"
        }]
    },
    "data": []
}

for tup in mapa1_df.itertuples():
    out['data'].append({
        'id': str(estados[tup.COD_ESTADO]),
        'value': str(tup.ESTADO_ORIGEM_COMPRA)
    })

@app.route('/map1')
def map1():
    return jsonify(out)

dado = {
    "chart": {
        "caption": "",
        "subcaption": "Estados x Quantidade",
        "xaxisname": "Estado",
        "yaxisname": "Unidades",
        "numbersuffix": "",
        "theme": "fusion",
    },
    "data": []
}

@app.route('/map1/SP')
def map1SP():
    dado['chart']['caption'] = 'São Paulo'
    dado['data'] = []

    for tup in mapa1_SP_df.itertuples():
        dado['data'].append({
            'label': str(tup.COD_ESTADO),
            'value': str(tup.UF)
        })

    return jsonify(dado)

@app.route('/map1/AL')
def map1AL():
    dado['chart']['caption'] = 'Alagoas'
    dado['data'] = []

    for tup in mapa1_AL_df.itertuples():
        dado['data'].append({
            'label': str(tup.COD_ESTADO),
            'value': str(tup.UF)
        })

    return jsonify(dado)

@app.route('/map1/BA')
def map1BA():
    dado['chart']['caption'] = 'Bahia'
    dado['data'] = []

    for tup in mapa1_BA_df.itertuples():
        dado['data'].append({
            'label': str(tup.COD_ESTADO),
            'value': str(tup.UF)
        })

    return jsonify(dado)

dado2 = {
    "chart": {
        "caption": "Disparidades",
        "subcaption": "Jun 2018",
        "includevalueinlabels": "1",
        "labelsepchar": ": ",
        "entityFillHoverColor": "#b5c23f",
        "theme": "fusion",
        "showLegend": "1"
    },
    "colorrange": {
        "minvalue": "0",
        "code": "#6baa01",
        "gradient": "1",
        "color": [{
            "maxvalue": 125,
            "code": "f8bd19"
        }, {
            "maxvalue": 250,
            "code": "e44a00"
        }]
    },
    "data": []
}

@app.route('/map2')
def map2():
    s = {}
    with open('inconsistencias.json', 'r') as file:
        s = json.loads(file.read())
    dado2['chart']['caption'] = 'Disparidades'
    for k, v in s.items():
        dado2['data'].append({
            'id': estados[k],
            'value': v
        })

    return jsonify(dado2)

def gen_dado3(name=None):
    dado3 = {
        "chart": {
            "caption": "Disparidades por Estado - " + name,
            "subcaption": "Jun 2018",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#b5c23f",
            "theme": "fusion",
            "showLegend": "1"
        },
        "colorrange": {
            "minvalue": "0",
            "code": "#6baa01",
            "gradient": "1",
            "color": [{
                "maxvalue": 500,
                "code": "f8bd19"
            }, {
                "maxvalue": 1000,
                "code": "e44a00"
            }]
        },
        "data": []
    }
    return dado3

s = {}
with open('inconsistencias_estado.json', 'r') as file:
    s = json.loads(file.read())


@app.route('/map2/SP')
def map2SP():
    dado3 = gen_dado3("São Paulo")
    for key in s['SP']:
        dado3['data'].append({
            'label':key,
            'value': s['SP'][key]
        })
    return jsonify(dado3)

@app.route('/map2/BA')
def map2BA():
    dado3 = gen_dado3("Bahia")
    for key in s['BA']:
        dado3['data'].append({
            'label':key,
            'value': s['BA'][key]
        })
    return jsonify(dado3)

@app.route('/map2/AL')
def map2AL():
    dado3 = gen_dado3("Alagoas")
    for key in s['AL']:
        dado3['data'].append({
            'label':key,
            'value': s['AL'][key]
        })
    return jsonify(dado3)

tabela = {}
with open('disparidades_tabela.json', 'r') as file:
    tabela = json.loads(json.loads(file.read()))

@app.route('/tabela')
def tabela_disparidades():
    return jsonify({ "data": tabela })
