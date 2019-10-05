# Rock Paper Scissors Lisard Spock
# By Steve Braich
#
# Sources:
#   https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from typing import List, Dict
from flask_cors import CORS
from json import JSONDecodeError
import lizardspock
import lizardspock_exceptions

#for debugging
import sys
from pprint import pprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class Choices(Resource):

    def get(self) -> List:
        return lizardspock.choices


class Choice(Resource):

    def get(self) -> Dict:
        return lizardspock.get_random_choice()


class Play(Resource):
    player: int

    def __init__(self) -> None:
        # json_data = request.get_json(force=True)
        # self.player = json_data['player']
        print('Hello world!', file=sys.stderr)
        print(request.headers, file=sys.stderr)
        pprint(request.headers, stream=sys.stderr)

        json_data = request.get_json(force=True)
        self.player = json_data['player']


        # try:
        #     json_data = request.get_json(force=True)
        #     self.player = json_data['player']
        # except TypeError as err:
        #     raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())
        # except JSONDecodeError as err:
        #     raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())
        # except Exception as err:
        #     raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())

    def post(self) -> Dict:
        # example {'results': 'win', 'player': 1, 'computer': 3}
        # result = lizardspock.play(self.player)
        # return result

        try:
            result = lizardspock.play(self.player)
            return result
        except IndexError as err:
            raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())


api.add_resource(Choices, '/choices')
api.add_resource(Choice, '/choice')
api.add_resource(Play, '/play')

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
    # app.run(debug=False)
    # app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
