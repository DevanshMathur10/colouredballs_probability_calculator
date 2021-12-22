import probability_calculator
import unittest

probability_calculator.random.seed(95)
class Tests(unittest.TestCase):
    def test_box_colourlist(self):
        box=probability_calculator.Box(black=3,yellow=4,purple=2)
        actual=box.colourlist
        expected=["black","black","black","yellow","yellow","yellow","yellow","purple","purple"]
        self.assertEqual(actual,expected,'Expected creation of box object to add correct contents.')

    def test_box_draw(self):
        box=probability_calculator.Box(black=5,yellow=4,purple=2)
        actual=box.draw(2)
        expected=['yellow','purple']
        self.assertEqual(actual,expected,'Expected box draw to return 2 random items from box contents.')
        actual=len(box.colourlist)
        expected=9
        self.assertEqual(actual,expected,'Expected box draw to reduce number of items in contents.')

    def test_box_experiment(self):
        box = probability_calculator.Box(pink=5,purple=2,orange=9)
        probability = probability_calculator.experiment(box=box, expected_balls={"pink":2,"purple":1}, balls_drawn=4, num_experiments=1000)
        actual = probability
        expected = 0.106
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
        box = probability_calculator.Box(pink=5,purple=1,white=3,orange=9,test=1)
        probability = probability_calculator.experiment(box=box, expected_balls={"pink":2,"orange":3,"test":1}, balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')       

if __name__ == "__main__":
    unittest.main()
