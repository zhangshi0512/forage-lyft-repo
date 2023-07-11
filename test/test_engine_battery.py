import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestBattery(unittest.TestCase):
    def test_nubbin_battery_service(self):
        # Test case where the battery needs service
        last_service_date = datetime(2018, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertEqual(battery.needs_service(), True)

        # Test case where the battery does not need service
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertEqual(battery.needs_service(), False)

    def test_spindler_battery_service(self):
        # Test case where the battery needs service
        last_service_date = datetime(2021, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertEqual(battery.needs_service(), True)

        # Test case where the battery does not need service
        last_service_date = datetime(2022, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertEqual(battery.needs_service(), False)


class TestEngine(unittest.TestCase):
    def test_capulet_engine_service(self):
        # Test case where the engine needs service
        current_mileage = 40000
        last_service_mileage = 5000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertEqual(engine.needs_service(), True)

        # Test case where the engine does not need service
        current_mileage = 20000
        last_service_mileage = 5000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertEqual(engine.needs_service(), False)

    def test_sternman_engine_service(self):
        # Test case where the warning light is on
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertEqual(engine.needs_service(), True)

        # Test case where the warning light is off
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertEqual(engine.needs_service(), False)

    def test_willoughby_engine_service(self):
        # Test case where the engine needs service
        current_mileage = 70000
        last_service_mileage = 5000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertEqual(engine.needs_service(), True)

        # Test case where the engine does not need service
        current_mileage = 50000
        last_service_mileage = 5000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertEqual(engine.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
