# Rock Paper Scissors Lisard Spock
# By Steve Braich
#
# Inspiration:
#   Flask RESTful Tutorial          https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from typing import List
from flask_cors import CORS
import flask_cors
import lizardspock
import json
#import jsonify
#from json import jsonify


# flask_cors.cross_origin()
# flask_cors.decorator.

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
#CORS(app, expose_headers='Authorization')
#api.decorators = [cors.crossdomain(origin='*', headers=['accept', 'Content-Type'])]
#api.decorators = [cors.crossdomain(origin='*', headers=['accept', 'Content-Type'])]
#app.config['CORS_HEADERS'] = 'Content-Type'

class Choices(Resource):

    def get(self) -> List:
        return lizardspock.choices


class Choice(Resource):

    def get(self) -> dict:
        return lizardspock.get_random_choice()


class Play(Resource):

    #@app.route("/api/v1/users/create", methods=['POST'])
    #@app.route("/play", methods=['POST'])
    def post(self) -> List:
        # request.headders.add()
        # request.headers.add('Access-Control-Allow-Origin', '*')
        # request.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        # request.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        # json_data = request.get_json()
        # print("json_data: {json_data}")
        # player = json_data['player']

        #data = json.loads(request.data)
        #player = data['player']

        #req = jsonify(request.form).json
        #request.form
        #player = request.form['player']

        #pippo = request.form.getlist('name[]')
        #player = request.form.getlist('player[]')

        #form = list(request.form.to_dict())[0]
        #player = json.loads(list(jsonify(request.form).json)[0])['player']
        computer = lizardspock.get_random_choice()['id']

        data = request.form.to_dict()
        player = json.loads(list(data)[0])['player']

        result = lizardspock.play(player, computer)
        return result

    # #@app.route("/api/v1/users/create", methods=['POST'])
    # #@app.route("/play", methods=['POST'])
    # def post(self) -> List:
    #     # request.headders.add()
    #     # request.headers.add('Access-Control-Allow-Origin', '*')
    #     # request.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    #     # request.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    #     json_data = request.get_json()
    #     print("json_data: {json_data}")
    #     player = json_data['player']
    #
    #     computer = lizardspock.get_random_choice()['id']
    #     result = lizardspock.play(player, computer)
    #     return result



api.add_resource(Choices, '/choices')
api.add_resource(Choice, '/choice')
api.add_resource(Play, '/play')


@app.after_request
def after_request(response):

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# @app.before_request
# def before_request():
    #request.headers['Origin']


# @app.before_request
# def option_autoreply():
#     """ Always reply 200 on OPTIONS request """
#
#     if request.method == 'OPTIONS':
#         resp = app.make_default_options_response()
#
#         headers = None
#         if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
#             headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']
#
#         h = resp.headers
#
#         # Allow the origin which made the XHR
#         h['Access-Control-Allow-Origin'] = request.headers['Origin']
#         # Allow the actual method
#         h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
#         # Allow for 10 seconds
#         h['Access-Control-Max-Age'] = "10"
#
#         # We also keep current headers
#         if headers is not None:
#             h['Access-Control-Allow-Headers'] = headers
#
#         return resp
#
#
# @app.after_request
# def set_allow_origin(resp):
#     """ Set origin for GET, POST, PUT, DELETE requests """
#
#     h = resp.headers
#
#     # Allow crossdomain for other HTTP Verbs
#     if request.method != 'OPTIONS' and 'Origin' in request.headers:
#         h['Access-Control-Allow-Origin'] = request.headers['Origin']
#
#
#     return resp


if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
    #app.run(debug=False)
    #app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)