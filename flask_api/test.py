from flask import Flask
from flask import jsonify
import pandas as pd
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
            "caption": "Mapa Show 1",
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

@app.route('/map1/SP')
def map1SP():
    dado = {
        "chart": {
            "caption": "Sao Paulo",
            "subcaption": "Extados x Quantidade",
            "xaxisname": "Estado",
            "yaxisname": "Unidades",
            "numbersuffix": "",
            "theme": "fusion"
        },
        "data": []
    }
    for tup in mapa1_SP_df.itertuples():
        dado['data'].append({
            'id': str(tup.COD_ESTADO),
            'value': str(tup.UF)
        })

    return jsonify(dado)

@app.route('/map1/AL')
def map1AL():
    dado = {
        "chart": {
            "caption": "Alagoas",
            "subcaption": "Extados x Quantidade",
            "xaxisname": "Estado",
            "yaxisname": "Unidades",
            "numbersuffix": "",
            "theme": "fusion"
        },
        "data": []
    }
    for tup in mapa1_AL_df.itertuples():
        dado['data'].append({
            'id': str(tup.COD_ESTADO),
            'value': str(tup.UF)
        })

    return jsonify(dado)

@app.route('/map1/BA')
def map1BA():
    dado = {
        "chart": {
            "caption": "Bahia",
            "subcaption": "Extados x Quantidade",
            "xaxisname": "Estado",
            "yaxisname": "Unidades",
            "numbersuffix": "",
            "theme": "fusion"
        },
        "data": []
    }
    for tup in mapa1_BA_df.itertuples():
        dado['data'].append({
            'id': str(tup.COD_ESTADO),
            'value': str(tup.UF)
        })

    return jsonify(dado)