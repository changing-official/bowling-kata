import unittest
from bowling.game import Game

class TestBowlingKata(unittest.TestCase):

    def testGameInstance(self):
        game = Game()
        self.assertIsNotNone(game)

    def testGameGutterballScoresZero(self):
        game = Game()
        for frame in range(10):
            game.addFrame(0, 0)

        self.assertEqual(game.score(), 0)

if __name__ == '__main__':
    unittest.main()