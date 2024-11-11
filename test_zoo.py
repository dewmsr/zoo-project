import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
    def test_baby_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)
    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(23), 150)
    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(127), 100)   
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()