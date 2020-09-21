from flask import Flask, jsonify, request
from flask_cors import CORS
from covid.api import CovId19Data
app = Flask(__name__)
api = CovId19Data(force=True)
res = api.filter_by_country("italy")
cors = CORS(app, resources={r"/api": {"origins": "*"}})
api = CovId19Data(force=False)
@app.route('/')
def index():
    return '<h1>index<h1><br><p>link to <a href="/api">api</a></p>'

@app.route('/api')
def api():
    return res



if __name__ == "__main__":
    app.run(debug=True)