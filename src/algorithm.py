player_strategies = ["car", "bus"]

def calculate_payoff(strategies):
    n_players = len(strategies)
    num_cars = strategies.count("car")
    num_buses = strategies.count("bus")

    payoffs = []

    for strat in strategies:
        if num_cars == n_players:
            payoffs.append(2)
        elif num_cars == 1 and strat == "car":
            payoffs.append(4)
        elif num_buses == 1 and strat == "bus":
            payoffs.append(1)
        elif num_buses == n_players:
            payoffs.append(3)
        else:
            payoffs.append(3)

    return payoffs



def main():
    n = input("Enter the number of students going to school? ")
    while not n.isdigit():
        print("Invalid input! Please try again.")
        n = input("Enter the number of students going to school? ")

    n = int(n)
    player_choies = []

    for i in range(n):
        strategy = input(f"Student {i+1}, choose your mode of transportation, car or bus? ")
        while strategy not in player_strategies:
            print("Invalid mode of transportation! Please try again.")
            strategy = input(f"Student {i+1}, choose your mode of transportation, car or bus? ")
        player_choies.append(strategy)

    game_points = calculate_payoff(player_choies)

    for i in range(n):
        print(f"Student {i+1} chose {player_choies[i]}. Payoff: {game_points[i]}")



if __name__ == "__main__":
    main()
