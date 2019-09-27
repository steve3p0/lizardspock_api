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
    upper = len(choices)
    random_c = random.randrange(1, upper)
    choice = [c for c in choices if c['id'] == random_c][0]
    return choice


def validate_choice(choice_id: int) -> None:
    if not isinstance(choice_id, int):
        raise TypeError(f"Invalid choice type. Expected 'int' got '{type(choice_id)}' instead.")

    lower = 1
    upper = len(choices)

    if not lower <= choice_id <= upper:
        raise IndexError(f"{choice_id} is an invalid choice id. Expecting 'int' between {lower} and {upper}.")


def play(player: int, computer: int) -> Dict:

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

def play1(player: int, computer: int) -> Dict:

    # Validate player and computer are existing choices
    validate_choice(player)
    validate_choice(computer)

    player -= 1
    computer -= 1

    if (computer + 1) % 5 == player:
        result = results.win
    elif (computer + 2) % 5 == player:
        result = results.win
    elif computer == player:
        result = results.tie
    else:
        result = results.lose

    res = {'results': result, 'player': player + 1, 'computer': computer + 1}
    return res