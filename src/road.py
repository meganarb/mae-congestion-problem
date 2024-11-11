class Player:
    def __init__(self, id):
        self.id = id
        self.delay = 0  # car has no delay (default..)
        
    def get_id(self):
        return 1 + self.id

    def set_delay(self, delay):
        self.delay = delay

class Road:
    def __init__(self, space):
        self.road_space = space
        self.bus_space = 2
        self.car_space = 1
        self.carPlayers = []
        self.busPlayers = []

    def add_car(self, player_obj):
        if player_obj.id not in self.carPlayer:
            self.carPlayers.append(id)
            return True
        return False
    
    def add_bus_player(self, player_obj):
        if player_obj.id not in self.busPlayers:
            self.busPlayers.append(id)
            return True
        return False
    
    def get_cars(self):
        return self.cars
    
    def get_busPlayres(self):
        return self.busPlayers

    def get_players(self):
        all_players = self.cars
        return all_players.extend(self.busPlayers)