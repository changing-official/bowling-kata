import unittest
from bowling.game import Game

class TestBowlingKata(unittest.TestCase):

    def testBowlingGameInstance(self):
        game = Game()
        self.assertIsNotNone(game)

if __name__ == '__main__':
    unittest.main()