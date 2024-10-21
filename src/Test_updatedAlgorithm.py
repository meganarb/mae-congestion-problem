import unittest
from updatedAlgorithm import *

class TestCalculateRoadFunc(unittest.TestCase):

    def test1(self):
        road = Road(20)

        road.add_buses(1)
        road.add_buses(2)
        road.add_buses(3)
        road.add_buses(4)
        road.add_buses(5)
        road.add_buses(6)
        road.add_buses(7)

        road.add_car(8)
        road.add_car(9)
        road.add_car(10)

        self.assertEqual(calculate_road(road), 0.35)
