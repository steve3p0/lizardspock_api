# Rock Paper Scissors Lizard Spock
# By Steve Braich
#
#   The Code Challenge              https://codechallenge.boohma.com/
#   The Big Bang Theory Episode     https://www.youtube.com/watch?v=YxVgzNYP45I

from collections import namedtuple
from typing import Dict
import random

Results = namedtuple('Results', 'win lose tie')
results = Results('win', 'lose', 'tie')
choices = [{'id': 1, 'name': 'rock'},
           {'id': 2, 'name': 'spock'},
           {'id': 3, 'name': 'paper'},
           {'id': 4, 'name': 'lizard'},
           {'id': 5, 'name': 'scissors'}]


def get_random_choice() -> Dict:
    """ Gets a random choice from the choices array of dict objects
    :return: Dict[choice], example { 'id': 2, 'name': 'spock' }
    """
    return random.choice(choices)


def validate_choice(choice_id: int) -> None:
    """ Validates that a move choice an int and within the range of acceptable values
    :param choice_id:
    :type choice_id: int
    :return:
    :rtype: None
    """
    if not isinstance(choice_id, int):
        raise TypeError(f"Invalid choice type. Expected 'int' got '{type(choice_id)}' instead.")

    lower = 1
    upper = len(choices)

    if not lower <= choice_id <= upper:
        raise IndexError(f"{choice_id} is an invalid choice id. Expecting 'int' between {lower} and {upper}.")


def play(player: int, computer: int = None) -> Dict:
    """ Decides who wins a round of rock paper scissors
    :param player:      The player choice id
    :param computer:    The computer choice id
    :return:            Dict[result] (example { 'results': 'win', 'player': 1, computer: 5 }
    """

    # If the computer choice has been passed already
    if computer is None:
        computer: int = get_random_choice()['id']

    # Validate player and computer are existing choices
    validate_choice(player)
    validate_choice(computer)

    if computer % 5 == player - 1:
        result = results.win
    elif (computer + 1) % 5 == player - 1:
        result = results.win
    elif computer == player:
        result = results.tie
    else:
        result = results.lose

    res = {'results': result, 'player': player, 'computer': computer}
    return res
