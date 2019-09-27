# Rock Paper Scissors Lizard Spock
# By Steve Braich

from unittest import TestCase
from lizardspock import results, choices
import lizardspock


class TestLizardSpock(TestCase):

    def test_get_random_choice(self):
        actual_choice = lizardspock.get_random_choice()
        self.assertTrue(actual_choice in choices)

    def test_play_post(self):
        input_player = 4    # lizard
        input_computer = 5  # spock

        expect_results = {'results': results.win, 'player': input_player, 'computer': input_computer}
        actual_results = lizardspock.play(input_player, input_computer)

        self.assertTrue(actual_results, expect_results)

    def test_play_post_regressive1(self):
        input_player = 1    # rock
        input_computer = 3  # paper

        actual_play = lizardspock.play(input_player, input_computer)
        self.assertTrue(isinstance(actual_play, dict))

        actual_results = actual_play['results']
        actual_player_choice_id = actual_play['player']
        actual_computer_choice_id = actual_play['computer']

        actual_player_choice = [c for c in choices if c['id'] == actual_player_choice_id][0]
        actual_computer_choice = [c for c in choices if c['id'] == actual_computer_choice_id][0]

        self.assertTrue(actual_results in results)
        self.assertTrue(actual_player_choice in choices)
        self.assertTrue(actual_computer_choice in choices)

    def test_play_post_regressive2(self):
        self.assertEqual(lizardspock.play(1, 1)['results'], results.tie)
        self.assertEqual(lizardspock.play(1, 2)['results'], results.lose)
        self.assertEqual(lizardspock.play(1, 3)['results'], results.lose)
        self.assertEqual(lizardspock.play(1, 4)['results'], results.win)
        self.assertEqual(lizardspock.play(1, 5)['results'], results.win)

        self.assertEqual(lizardspock.play(2, 1)['results'], results.win)
        self.assertEqual(lizardspock.play(2, 2)['results'], results.tie)
        self.assertEqual(lizardspock.play(2, 3)['results'], results.lose)
        self.assertEqual(lizardspock.play(2, 4)['results'], results.lose)
        self.assertEqual(lizardspock.play(2, 5)['results'], results.win)

        self.assertEqual(lizardspock.play(3, 1)['results'], results.win)
        self.assertEqual(lizardspock.play(3, 2)['results'], results.win)
        self.assertEqual(lizardspock.play(3, 3)['results'], results.tie)
        self.assertEqual(lizardspock.play(3, 4)['results'], results.lose)
        self.assertEqual(lizardspock.play(3, 5)['results'], results.lose)

        self.assertEqual(lizardspock.play(4, 1)['results'], results.lose)
        self.assertEqual(lizardspock.play(4, 2)['results'], results.win)
        self.assertEqual(lizardspock.play(4, 3)['results'], results.win)
        self.assertEqual(lizardspock.play(4, 4)['results'], results.tie)
        self.assertEqual(lizardspock.play(4, 5)['results'], results.lose)

        self.assertEqual(lizardspock.play(5, 1)['results'], results.lose)
        self.assertEqual(lizardspock.play(5, 2)['results'], results.lose)
        self.assertEqual(lizardspock.play(5, 3)['results'], results.win)
        self.assertEqual(lizardspock.play(5, 4)['results'], results.win)
        self.assertEqual(lizardspock.play(5, 5)['results'], results.tie)

    def test_play_post_invalid_choice_wrongtype(self):
        input_player = '1'
        input_computer = 4

        with self.assertRaises(TypeError):
            actual_play = lizardspock.play(input_player, input_computer)

    def test_play_post_invalid_choice_outofrange(self):
        input_player = 999
        input_computer = 4

        with self.assertRaises(IndexError):
            actual_play = lizardspock.play(input_player, input_computer)
