from newRoad import *
import math
import random

player_strategies = ["1", "2"]

def calculate_road(road):
    road_taken = len(road.carPlayers) + len(road.busPlayers) * 2  # Buses take twice the space
    return road_taken / road.road_space

def F(x):
    t = 0.5  # Threshold
    L = 10   # Maximum delay
    c = 10   # Congestion factor
    return min(L, c * x)

def calculate_bus_delay(road):
    road_space = road.road_space
    cars = len(road.get_cars())
    buses = len(road.get_busPlayers())
    Sc = road.car_space  # Space taken by a car
    Sb = road.bus_space  # Space taken by a bus
    B = 2  # Fixed delay for buses

    # Formula: F((Sc * C) / R) + B + (Sb / R)
    congestion_factor = (Sc * cars) / road_space
    return F(congestion_factor) + B + (Sb / road_space)

def calculate_car_delay(road):
    road_space = road.road_space
    cars = len(road.get_cars())
    buses = len(road.get_busPlayers())
    Sc = road.car_space  # Space taken by a car
    Sb = road.bus_space  # Space taken by a bus

    # Formula: F((Sc * C / R) + (Sc / R)) + (Sb / R)
    congestion_factor = (Sc * cars) / road_space
    return F(congestion_factor + Sc / road_space) + (Sb / road_space)


def switch_strategy(road):
    for player in road.get_players():
        if player in road.carPlayers and random.random() < 0.3:
            road.add_bus_player(player)
            road.carPlayers.remove(player)
            print(f"Player {player.get_id()} switches to bus.")
        elif player in road.busPlayers and random.random() < 0.3:
            road.add_car(player)
            road.busPlayers.remove(player)
            print(f"Player {player.get_id()} switches to car.")

def main():
    road_space = int(input("Enter the amount of road space: "))
    n = int(input("Enter the number of students going to school: "))
    rounds = int(input("Enter the number of days to simulate: "))
    allow_switching = input("Allow strategy switching? (y/n): ").lower() == 'y'

    road = Road(road_space)

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

    for day in range(rounds):
        print(f"\nDay {day + 1}: ")
        congestion_lvl = calculate_road(road)
        print(f"Amount of road taken up: {congestion_lvl * 100:.2f}%.")

        for player in road.get_players():
            if player in road.carPlayers:
                player.set_delay(calculate_car_delay(road))
            else:
                player.set_delay(calculate_bus_delay(road))
            print(f"Player {player.get_id()}: Delay = {player.delay:.2f}")
        
        if allow_switching:
            switch_strategy(road)

if __name__ == "__main__":
    main()