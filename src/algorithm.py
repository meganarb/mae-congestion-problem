from newRoad import *
import math
import random

# 1: Car, 2: Bus
player_strategies = ["1", "2"]
#players_dict = {}

def calculate_road(road):
    road_taken = 0
    road_space = road.road_space

    for i in range(len(road.carPlayers)):
        road_taken = road_taken + 1

    return road_taken/road_space

def F(x):
    t = 0
    L = 0
    c = 0
    if x > t: return L
    else: return c*x

def calculate_bus_delay(road):
    road_space = road.road_space
    cars = len(road.get_cars())
    buses = 0 #change
    Sc = road.car_space
    Sb = road.bus_space * buses
    delay = 0 #change
    return F(Sc * cars / road_space) + delay + Sb / road_space

def calculate_car_delay(road):
    road_space = road.road_space
    cars = len(road.get_cars())
    buses = 0 #change
    Sc = road.car_space
    Sb = road.bus_space * buses
    delay = 0 #change
    return F(((Sc * cars) / road_space) + (Sc / road_space)) + (Sb / road_space)

# first iteration of switching stategy function
def switch_strategy(road, congestion_lvl):
    threshhold = 50.0 #threshold
    # maybe adjust delays if threshold met

    if(road.space // len(road.carPlayers)):
        for player in road.get_players:
            if player in road.carPlayers:
                if random.random() < 0.7:
                    print("Switch to bus")
                    road.add_bus_playe(player)
                    road.carPlayers.remove(player)
            elif player in road.busPlayers:
                if random.random() < 0.7:
                    print("Switch to car")
                    road.add_bus_player(player)
                    road.busPlayers.remove(player)


def main():
    road = int(input("Enter the amount of road space: "))
    # while not road.isdigit():
    #     print("Invalid input! Please try again.")
    #     road = input("Enter a number!")

    road_space = Road(road)


    n = int(input("Enter the number of students going to school? "))
    # while not n.isdigit():
    #     print("Invalid input! Please try again.")
    #     n = input("Enter the number of students going to school? ")

    rounds = int(input("Enter the number of days to simulate: "))

    player_choices = []

    for i in range(n):
        strategy = input(f"Student {i+1}, choose your mode of transportation | Car(1) or Bus(2)? ")
        while strategy not in player_strategies:
            print("Invalid mode of transportation! Please try again.")
            strategy = input(f"Student {i+1}, choose your mode of transportation | Car(1) or Bus(2)? ")
        player_choices.append(strategy)

    counter = 0
    for i in player_choices:
        # 1: CAR
        if i == '1':
            road_space.add_car(Player(counter))
            counter = counter + 1
        # 2: BUS
        if i == '2':
            road_space.add_bus_player(Player(counter))
            counter = counter + 1

    for day in range(rounds):
        print(f"\nDay {day + 1}: ")
        congestion_lvl = calculate_road(road_space)
        print(f"Amount of road taken up: {congestion_lvl * 100}%.")

        for player in road_space.get_players():
            print(f"Player {player.id}: {player.delay}")
        switch_strategy(road_space, congestion_lvl)

if __name__ == "__main__":
    main()
