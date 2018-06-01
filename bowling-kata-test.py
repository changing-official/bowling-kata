import unittest
from bowling.game import Game

class TestBowlingKata(unittest.TestCase):

    @classmethod
    def setUp(self):
       self.game = Game()

    def testGameInstance(self):
        self.assertIsNotNone(self.game)

    def testGameGutterballScoresZero(self):
        for frame in range(10):
            self.game.addFrame(0, 0)

        self.assertEqual(self.game.score(), 0)

if __name__ == '__main__':
    unittest.main()
