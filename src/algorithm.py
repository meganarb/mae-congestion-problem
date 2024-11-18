from newRoad import *
import math
import random

# 1: Car, 2: Bus
player_strategies = ["1", "2"]

# Function to calculate the percentage of road taken up by cars and buses
def calculate_road(road):
    road_taken = len(road.carPlayers) + 5 * 2  # Buses take twice the space
    return road_taken / road.road_space

# Function F(x) that calculates delay based on congestion factor
def F(x):
    t = 0.5  # Threshold
    L = 10   # Maximum delay
    c = 10   # Congestion factor
    return min(L, c * x)

# Function to calculate bus delay based on the formula provided in the image
def calculate_bus_delay(road):
    road_space = road.road_space
    cars = len(road.get_cars())
    buses = len(road.get_busPlayers())
    Sc = road.car_space  # Space taken by a car (should be 1)
    Sb = road.bus_space  # Space taken by a bus (should be 2)
    B = 2  # Fixed delay for buses

    # Formula: F((Sc * C) / R) + B + (Sb / R)
    congestion_factor = (Sc * cars) / road_space
    return F(congestion_factor) + B + (Sb / road_space)

# Function to calculate car delay based on the formula provided in the image
def calculate_car_delay(road):
    road_space = road.road_space
    cars = len(road.get_cars())
    buses = len(road.get_busPlayers())
    Sc = road.car_space  # Space taken by a car (should be 1)
    Sb = road.bus_space  # Space taken by a bus (should be 2)

    # Formula: F((Sc * C / R) + (Sc / R)) + (Sb / R)
    congestion_factor = (Sc * cars) / road_space
    return F(congestion_factor + Sc / road_space) + (Sb / road_space)

# Function to switch strategies for players randomly between car and bus
def switch_strategy(road):
    current_congestion = calculate_road(road)
    for player in road.get_players():
        if current_congestion > 0.60:
            if player in road.carPlayers and random.random() < 0.3:
                road.add_bus_player(player)
                road.carPlayers.remove(player)
                print(f"Player {player.get_id()} switches to bus.")
        elif player in road.busPlayers and random.random() < 0.3:
            road.add_car(player)
            road.busPlayers.remove(player)
            print(f"Player {player.get_id()} switches to car.")


# Main function to run the simulation
def main():
    # Input for initial setup
    road_space = int(input("Enter the amount of road space: "))
    n = int(input("Enter the number of students going to school: "))
    rounds = int(input("Enter the number of days to simulate: "))
    allow_switching = input("Allow strategy switching? (y/n): ").lower() == 'y'

    # Create a new Road object with the specified space
    road = Road(road_space)

    # Initial player setup: Each student chooses their mode of transportation (car or bus)
    for i in range(n):
        strategy = input(f"Student {i+1}, choose your mode of transportation | Car(1) or Bus(2)? ")
        while strategy not in player_strategies:
            print("Invalid mode of transportation! Please try again.")
            strategy = input(f"Student {i+1}, choose your mode of transportation | Car(1) or Bus(2)? ")
        
        player = Player(i)
        if strategy == '1':
            road.add_car(player)
        else:
            road.add_bus_player(player)

    # Simulate multiple rounds (days)
    for day in range(rounds):
        print(f"\nDay {day + 1}: ")

        # Calculate congestion level based on current players
        congestion_lvl = calculate_road(road)
        print(f"Amount of road taken up: {congestion_lvl * 100:.2f}%.")

        # Calculate delays for all players based on their current mode of transportation
        for player in road.get_players():
            if player in road.carPlayers:
                player.set_delay(calculate_car_delay(road))
            else:
                player.set_delay(calculate_bus_delay(road))
            print(f"Player {player.get_id()}: Delay = {player.delay:.2f}")
        
        # Switch strategies if allowed
        if allow_switching:
            switch_strategy(road)

        # Recalculate congestion and delays after switching strategies, if applicable
        if allow_switching:
            print("\nAfter switching:")
            congestion_lvl = calculate_road(road)
            print(f"New amount of road taken up: {congestion_lvl * 100:.2f}%.")

            for player in road.get_players():
                if player in road.carPlayers:
                    player.set_delay(calculate_car_delay(road))
                else:
                    player.set_delay(calculate_bus_delay(road))
                print(f"Player {player.get_id()}: New Delay = {player.delay:.2f}")

if __name__ == "__main__":
    main()
