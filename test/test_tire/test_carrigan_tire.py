import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_service(self):
        # Test case where the tire needs service
        tire_wear_array = [0.1, 0.1, 0.9, 0.1]
        tire = CarriganTire(tire_wear_array)
        self.assertEqual(tire.needs_service(), True)

        # Test case where the tire does not need service
        tire_wear_array = [0.1, 0.1, 0.8, 0.1]
        tire = CarriganTire(tire_wear_array)
        self.assertEqual(tire.needs_service(), False)
