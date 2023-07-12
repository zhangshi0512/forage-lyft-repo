import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_service(self):
        # Test case where the tire needs service
        tire_wear_array = [0.8, 0.8, 0.8, 0.8]
        tire = OctoprimeTire(tire_wear_array)
        self.assertEqual(tire.needs_service(), True)

        # Test case where the tire does not need service
        tire_wear_array = [0.7, 0.7, 0.7, 0.7]
        tire = OctoprimeTire(tire_wear_array)
        self.assertEqual(tire.needs_service(), False)
