import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("clubs", 1)
        self.card_2 = Card("clubs", 2)
        self.card_game = CardGame()


    def test_if_card_value_is_1(self):
        self.card_game.check_for_ace(self.card_1)
        self.assertEqual(True, self.card_1.value)

    def test_which_card_highest(self):
        self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(2, self.card_2.value)

    def test_what_is_total_of_cards(self):
        cards = [self.card_1, self.card_2]
        self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 3", self.card_game.cards_total(cards))