import unittest
from newRoad import Road, Player
from algorithm import calculate_road, calculate_bus_delay, calculate_car_delay

class TestCalculateRoadFunc(unittest.TestCase):
    def test_road_usage(self):
        road = Road(20)
        print("\nTEST 1: Road Usage with 20 units of road space")
        for i in range(7):
            road.add_bus_player(Player(i))
        for i in range(7, 10):
            road.add_car(Player(i))
        
        road_usage = calculate_road(road)
        print(f"Amount of road taken up: {road_usage * 100:.2f}%")
        self.assertAlmostEqual(road_usage, 0.85, places=2)

class TestCalculateBusDelay(unittest.TestCase):
    def test_bus_delay(self):
        road = Road(20)
        print("\nTEST 2: Bus Delay with 5 buses and 5 cars on a 20-unit road")
        for i in range(5):
            road.add_bus_player(Player(i))
        for i in range(5, 10):
            road.add_car(Player(i))

        bus_delay = calculate_bus_delay(road)
        print(f"Calculated Bus Delay: {bus_delay:.2f}")
        self.assertAlmostEqual(bus_delay, 4.6, delta=0.5)

class TestCalculateCarDelay(unittest.TestCase):
    def test_car_delay(self):
        road = Road(20)
        print("\nTEST 3: Car Delay with 5 cars and 2 buses on a 20-unit road")
        for i in range(5):
            road.add_car(Player(i))
        for i in range(5, 7):
            road.add_bus_player(Player(i))

        car_delay = calculate_car_delay(road)
        print(f"Calculated Car Delay: {car_delay:.2f}")
        self.assertAlmostEqual(car_delay, 3.1, delta=0.35)

# New Tests to Compare Delays with Different Numbers of Cars

class TestBusAndCarDelaysComparison(unittest.TestCase):
    def test_delays_with_5_buses_and_2_cars(self):
        road = Road(20)
        print("\nTEST 4: Bus and Car Delays with 5 buses and 2 cars on a 20-unit road")
        
        # Adding players
        for i in range(5):   # Add 5 buses
            road.add_bus_player(Player(i))
        
        for i in range(2):   # Add 2 cars
            road.add_car(Player(i + 5))
        
        # Calculating delays
        bus_delay = calculate_bus_delay(road)
        car_delay = calculate_car_delay(road)
        
        # Print results
        print(f"Calculated Bus Delay (5 buses, 2 cars): {bus_delay:.2f}")
        print(f"Calculated Car Delay (5 buses, 2 cars): {car_delay:.2f}")

    def test_delays_with_5_buses_and_10_cars(self):
        road = Road(20)
        print("\nTEST 5: Bus and Car Delays with 5 buses and 10 cars on a 20-unit road")
        
        # Adding players
        for i in range(5):   # Add 5 buses
            road.add_bus_player(Player(i))
        
        for i in range(10):   # Add 10 cars
            road.add_car(Player(i + 5))
        
        # Calculating delays
        bus_delay = calculate_bus_delay(road)
        car_delay = calculate_car_delay(road)
        
        # Print results
        print(f"Calculated Bus Delay (5 buses, 10 cars): {bus_delay:.2f}")
        print(f"Calculated Car Delay (5 buses, 10 cars): {car_delay:.2f}")

if __name__ == '__main__':
    unittest.main()