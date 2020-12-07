from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
'''
{
  "confirmed": 1728878,
  "deaths": 60078,
  "label": "Italy",
  "last_updated": "2020-12-06 00:00:00",
  "lat": "41.87194",
  "long": "12.56738",
  "recovered": 913494
}
'''

allow_cors = [#cors site
    "https://www.liceocremonablog.it",
    "http://www.liceocremonablog.it"
]
app = Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": allow_cors},r"/v2/api": {"origins": allow_cors},r"/v2/api/complete": {"origins": allow_cors},r"/v1/api": {"origins": allow_cors} })
@app.route('/')#app index
def index():
    return '<h1>index<h1><br><p>link to <a href="/v2/api">api</a></p>'

@app.route('/v1/api')#old api url
def api_old():
    return jsonify({"body": "questa versione non è più disponibile"})

@app.route('/v2/api')#new api url based on offical datas
@app.route('/api')
def api():
    raw_json = requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json").json()
    today_data = raw_json[(len(raw_json)-1)]
    api_dict = {
        "confirmed": today_data["totale_casi"],
        "deaths": today_data["deceduti"],
        "recovered": today_data["dimessi_guariti"],
        "last_updated": today_data["data"],
        "label": today_data["stato"]
    }
    return jsonify(api_dict)
    
@app.route('/v2/api/complete')#complete officail datas
def api_or():
    raw_json = requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json").json()
    today_data = raw_json[(len(raw_json)-1)]
    return jsonify(today_data)

if __name__ == "__main__":
    app.run(debug=True)