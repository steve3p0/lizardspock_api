# Rock Paper Scissors Lizard Spock
# By Steve Braich
#
# Inspiration:
#   https://stackoverflow.com/questions/7428124/how-can-i-fake-request-post-and-get-params-for-unit-testing-in-flask
#   https://flask.palletsprojects.com/en/1.0.x/testing/

from unittest import TestCase
import json
from app import app
import lizardspock


# Integration Tests
class TestApp(TestCase):

    def setUp(self):
        self.expect_status_code = 200
        self.expect_choices = lizardspock.choices
        self.expect_results = lizardspock.results

        self.input_content_type = 'application/json'
        self.client = app.test_client()

    def test_choices_get(self):
        input_url = '/choices'

        actual_response = self.client.get(input_url)
        self.assertEqual(actual_response.status_code, self.expect_status_code)
        self.assertEqual(actual_response.json, self.expect_choices)

    # Edge Testing: This test is here just to see the expected behavior
    # I may try to trap these errors and give a more meaningful error message
    def test_choices_invalid_param(self):
        input_url = '/choices/1'

        expect_status_code = 404
        expect_choices = None

        actual_response = self.client.get(input_url)
        self.assertEqual(actual_response.status_code, expect_status_code)
        self.assertEqual(actual_response.json, expect_choices)

    def test_choice_get(self):
        input_url = '/choice'

        actual_response = self.client.get(input_url)
        self.assertEqual(actual_response.status_code, self.expect_status_code)
        actual_choice = json.loads(actual_response.data)
        self.assertTrue(actual_choice in self.expect_choices)

    def test_play_post(self):
        input_route = '/play'
        input_json = {'player': 1}

        actual_response = self.client.post(input_route, json=input_json)
        self.assertEqual(actual_response.status_code, self.expect_status_code)

        # Type Hint: <class 'dict'>: {'results': 'win', 'player': 1, 'computer': 4}
        actual_play = json.loads(actual_response.data)
        self.assertTrue(isinstance(actual_play, dict))

        actual_results = actual_play['results']
        actual_player_choice_id = actual_play['player']
        actual_computer_choice_id = actual_play['computer']

        actual_player_choice = [c for c in self.expect_choices if c['id'] == actual_player_choice_id][0]
        actual_computer_choice = [c for c in self.expect_choices if c['id'] == actual_computer_choice_id][0]

        self.assertTrue(actual_results in self.expect_results)
        self.assertTrue(actual_player_choice in self.expect_choices)
        self.assertTrue(actual_computer_choice in self.expect_choices)

    def test_play_post_invalid_choice_outofrange(self):
        input_url = '/play'
        input_data = json.dumps({'player': 999})

        expect_status_code = 404

        actual_response = self.client.post(input_url, data=input_data, content_type=self.input_content_type)
        self.assertEqual(actual_response.status_code, expect_status_code)

        # Type Hint: <class 'dict'>: {'results': 'win', 'player': 1, 'computer': 4}
        actual_play = json.loads(actual_response.data)
        self.assertTrue(isinstance(actual_play, dict))

        actual_results = actual_play['results']
        actual_player_choice_id = actual_play['player']
        actual_computer_choice_id = actual_play['computer']

        actual_player_choice = [c for c in self.expect_choices if c['id'] == actual_player_choice_id][0]
        actual_computer_choice = [c for c in self.expect_choices if c['id'] == actual_computer_choice_id][0]

        self.assertTrue(actual_results in self.expect_results)
        self.assertTrue(actual_player_choice in self.expect_choices)
        self.assertTrue(actual_computer_choice in self.expect_choices)

    def test_play_post_invalid_choice_wrongtype(self):
        input_url = '/play'
        input_data = json.dumps({'player': 'XXX'})

        expect_status_code = 400    # BAD REQUEST

        actual_response = self.client.post(input_url, data=input_data, content_type=self.input_content_type)
        self.assertEqual(actual_response.status_code, expect_status_code)

        # Type Hint: <class 'dict'>: {'results': 'win', 'player': 1, 'computer': 4}
        actual_play = json.loads(actual_response.data)
        self.assertTrue(isinstance(actual_play, dict))

        actual_results = actual_play['results']
        actual_player_choice_id = actual_play['player']
        actual_computer_choice_id = actual_play['computer']

        actual_player_choice = [c for c in self.expect_choices if c['id'] == actual_player_choice_id][0]
        actual_computer_choice = [c for c in self.expect_choices if c['id'] == actual_computer_choice_id][0]

        self.assertTrue(actual_results in self.expect_results)
        self.assertTrue(actual_player_choice in self.expect_choices)
        self.assertTrue(actual_computer_choice in self.expect_choices)