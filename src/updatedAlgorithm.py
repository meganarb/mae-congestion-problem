from road import *
import math

# 1: Car, 2: Bus
player_strategies = ["1", "2"]
#players_dict = {}

def calculate_road(road):
    road_taken = 0
    road_space = road.space


    for i in range(len(road.get_buses())):
        road_taken = road_taken + 2

    for i in range(len(road.get_cars())):
        road_taken = road_taken + 1

    return road_taken/road_space

def calculate_bus_payoff(road):
    road_space = road.get_space()

    if len(road.get_buses()) > 0:
        bus_space = road.get_buses()[0].get_road_space()
        num_bus = len(road.get_buses())
    else:
        bus_space = 0
        num_bus = 0

    if len(road.get_cars()) > 0:
        car_space = road.get_cars()[0].get_road_space()
        num_car = len(road.get_cars())
    else:
        car_space = 0
        num_car = 0

    # completely arbitrary, can change or remove
    bus_delay = road_space * 0.05

    payoff = (road_space - (bus_space * num_bus + car_space * num_car + bus_delay)) / road_space

    if payoff > 0: return payoff
    return 0


def calculate_car_payoff(road):
    road_space = road.get_space()

    if len(road.get_buses()) > 0:
        bus_space = road.get_buses()[0].get_road_space()
        num_bus = len(road.get_buses())
    else:
        bus_space = 0
        num_bus = 0

    if len(road.get_cars()) > 0:
        car_space = road.get_cars()[0].get_road_space()
        num_car = len(road.get_cars())
    else:
        car_space = 0
        num_car = 0

    payoff = (road_space - (bus_space * num_bus + car_space * (num_car - 1))) / road_space
    if payoff > 0: return payoff
    return 0

def calculate_payoffs(road):

    bus_payoff = calculate_bus_payoff(road)
    car_payoff = calculate_car_payoff(road)

    for bus in road.get_buses():
        for commuter in bus.get_players():
            commuter.set_payoff(bus_payoff)

    for car in road.get_cars():
        car.get_players()[0].set_payoff(car_payoff)


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
            road_space.add_car(counter)
            counter = counter + 1
        # 2: BUS
        if i == '2':
            road_space.add_buses(counter)
            counter = counter + 1

    game_space_taken = calculate_road(road_space)

    print(f"This is the amount of road taken up: {game_space_taken * 100}%.")

    calculate_payoffs(road_space)

    print("Payoffs:")
    for player in road_space.get_players():
        print(f"Player {player.get_id()}: {player.get_payoff()}")


if __name__ == "__main__":
    main()
