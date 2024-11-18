import unittest
from newRoad import Road, Player
from algorithm import calculate_road, calculate_bus_delay, calculate_car_delay, switch_strategy

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
        self.assertAlmostEqual(road_usage, 0.65, places=2)

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

# New Test Case to Illustrate Strategy Switching

class TestStrategySwitching(unittest.TestCase):
    def test_strategy_switching(self):
        # Initial setup
        road_space = 20
        num_players = 10
        rounds = 8
        allow_switching = True
        
        print("\nTEST 4: Strategy Switching over multiple rounds")

        # Create the road
        road = Road(road_space)

        # Add initial players (half cars, half buses)
        for i in range(num_players // 2):
            road.add_car(Player(i))
        
        for i in range(num_players // 2, num_players):
            road.add_bus_player(Player(i))

        # Simulate multiple rounds with strategy switching
        for day in range(rounds):
            print(f"\nDay {day + 1}: ")
            
            # Calculate congestion level
            congestion_lvl = calculate_road(road)
            print(f"Amount of road taken up: {congestion_lvl * 100:.2f}%.")

            # Calculate delays for all players
            for player in road.get_players():
                if player in road.carPlayers:
                    player.set_delay(calculate_car_delay(road))
                else:
                    player.set_delay(calculate_bus_delay(road))
                print(f"Player {player.get_id()}: Delay = {player.delay:.2f}")
            
            # Switch strategies if allowed
            if allow_switching:
                switch_strategy(road)

if __name__ == '__main__':
    unittest.main()
