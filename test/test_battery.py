import unittest

from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        test_battery = NubbinBattery(
            today, today.replace(year=today.year - 5))
        self.assertTrue(test_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        test_battery = SpindlerBattery(
            today, today.replace(year=today.year - 1))
        self.assertFalse(test_battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        test_battery = SpindlerBattery(
            today, today.replace(year=today.year - 5))
        self.assertTrue(test_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        test_battery = SpindlerBattery(
            today, today.replace(year=today.year - 1))
        self.assertFalse(test_battery.needs_service())
