import unittest
import os
from geobricks_geocoding.core.geocoding_core import get_locations


class GeobricksTest(unittest.TestCase):

    def test_get_locations(self):
        location = get_locations(["Rome"])
        self.assertEqual(location, [[41.8933439, 12.4830718]])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)