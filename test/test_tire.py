import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_worn = [0.9, 0.9, 0.9, 0.9]
        test_tire = CarriganTire(tire_worn)
        self.assertTrue(test_tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_worn = [0.8, 0.8, 0.8, 0.8]
        test_tire = CarriganTire(tire_worn)
        self.assertFalse(test_tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_worn = [1, 1, 1, 1]
        test_tire = OctoprimeTire(tire_worn)
        self.assertTrue(test_tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_worn = [0.2, 0.2, 0.1, 0.1]
        test_tire = OctoprimeTire(tire_worn)
        self.assertFalse(test_tire.needs_service())
