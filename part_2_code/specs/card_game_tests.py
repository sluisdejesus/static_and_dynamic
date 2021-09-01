import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.cardgame = CardGame
        self.card1 = Card("clubs",1)
        self.card2 = Card("diamonds",5)
        self.card3 = Card("spades",10)
        self.card4 = Card("hearts",3)
        self.cards = [self.card1,self.card2, self.card3, self.card4]

    def test__check_for_ace(self):
        test_result = self.cardgame.check_for_ace(self, self.card1)
        self.assertTrue(test_result)

    def test__highest_card(self):
        test_result = self.cardgame.highestcard(self, self.card2,self.card3)
        self.assertEqual(self.card3, test_result)

    def test__cards_total(self):
        test_result = self.cardgame.cards_total(self,self.cards)
        self.assertEqual("You have a total of" + str(19), test_result)    
