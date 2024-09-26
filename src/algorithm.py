player_strategies = ["car", "bus"]

def calculate_payoff(strategies):
    n_players = len(strategies)
    num_cars = strategies.count("car")
    num_buses = strategies.count("bus")

    final_points = [0] * n_players

    for i in range(n_players):
        if strategies[i] == 'car':
            final_points[i] = max(2 - num_cars, 0) + 2
        elif strategies[i] == 'bus':
            final_points[i] = 3 + num_buses

    return final_points

def get_player_strategy(player_num):
    while True:
        strategy = input(f"Player {player_num}, choose your mode of transportation, car of bus?").capitalize()

def main():
    n = int(input("Enter teh number of students going to school?"))
    player_choies = []

    for i in range(n):
        strategy = input(f"Player {i+1}, choose your mode of transportation, car or bus? ")
        while strategy not in player_strategies:
            print("Invalid mode of transportation! Please try again.")
            strategy = input(f"Player {i+1}, choose your mode of transportation, car or bus? ")
        player_choies.append(strategy)

    game_points = calculate_payoff(player_choies)

    for i in range(n):
        print(f"Player {i+1} chose {player_choies[i]}. Payoff: {game_points[i]}")

if __name__ == "__main__":
    main()