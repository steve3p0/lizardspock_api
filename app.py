# Rock Paper Scissors Lisard Spock
# By Steve Braich
#
# Inspiration:
#   Flask RESTful Tutorial          https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

from flask import Flask, request
from flask_restful import Resource, Api
from typing import List
import lizardspock

app = Flask(__name__)
api = Api(app)

class Choices(Resource):

    def get(self) -> List:
        return lizardspock.choices


class Choice(Resource):

    def get(self) -> dict:
        return lizardspock.get_random_choice()


class Play(Resource):

    def post(self) -> List:
        json_data = request.get_json()
        player = json_data['player']

        computer = lizardspock.get_random_choice()['id']
        result = lizardspock.play(player, computer)
        return result

api.add_resource(Choices, '/choices')
api.add_resource(Choice, '/choice')
api.add_resource(Play, '/play')


if __name__ == '__main__':
    app.run(debug=True)
