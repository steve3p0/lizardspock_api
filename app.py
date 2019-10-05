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

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class Choices(Resource):
    """ Encapsulates an abstract RESTful resource for getting the list of choices """

    def get(self) -> List:
        """ HTTP GET call that retrieves a list of available choices for the game
        :return: Dict[result] (example { 'results': 'win', 'player': 1, computer: 5 }
        """
        return lizardspock.choices


class Choice(Resource):
    """ Encapsulates an abstract RESTful resource for getting a random choice """

    def get(self) -> Dict:
        """ HTTP GET call that gets a random choice for the game
        :return: Dict[choice], example { 'id': 2, 'name': 'spock' }
        """
        return lizardspock.get_random_choice()


class Play(Resource):
    """ Encapsulates an abstract RESTful resource for POSTing a play (round) of the game """

    player: int

    def __init__(self) -> None:
        """ Constructor for Play class that sets up an HTTP POST """
        try:
            json_data = request.get_json(force=True)
            self.player = json_data['player']
        except TypeError as err:
            raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())
        except JSONDecodeError as err:
            raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())
        except Exception as err:
            raise lizardspock_exceptions.InvalidUsage(err.message, 400, request.get_data())

    def post(self) -> Dict:
        """ HTTP POST call that plays a game
        :return: Dict[result] (example { 'results': 'win', 'player': 1, computer: 5 }
        :rtype: Union[Dict[str, str], None]
        """

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
