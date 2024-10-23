import unittest

from numpy.ma.testutils import assert_equal

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


    def test2(self):
        road = Road(10)

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

        self.assertEqual(calculate_road(road), 0.7)

    def test3(self):
        road = Road(40)

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

        self.assertEqual(calculate_road(road), .175)


class TestCalculateBusPayoff(unittest.TestCase):

    def testHalfRoad(self):
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

        self.assertEqual(calculate_bus_payoff(road), 0.65)

    def testOnlyOneBus(self):

        road = Road(20)

        road.add_buses(1)
        road.add_buses(2)
        road.add_buses(3)

        self.assertEqual(calculate_bus_payoff(road), 0.9)


class TestCalculateCarPayoff(unittest.TestCase):

    def testOneCar(self):

        road = Road(20)

        road.add_car(1)

        self.assertEqual(calculate_car_payoff(road), 1)


    def testFiveCar(self):

        road = Road(20)
        road.add_car(1)
        road.add_car(2)
        road.add_car(3)
        road.add_car(4)
        road.add_car(5)

        self.assertEqual(calculate_car_payoff(road), 0.8)


    def testRoadFull(self):

        road = Road(10)

        road.add_car(1)
        road.add_car(2)
        road.add_car(3)
        road.add_car(4)
        road.add_car(5)
        road.add_car(6)

        road.add_buses(6)
        road.add_buses(7)
        road.add_buses(8)
        road.add_buses(9)
        road.add_buses(10)
        road.add_buses(11)
        road.add_buses(12)

        self.assertEqual(calculate_car_payoff(road), 0)