class Player:
    def __init__(self, id):
        self.id = id
        self.delay = 0
        
    def get_id(self):
        return self.id

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
        if player_obj not in self.carPlayers:
            self.carPlayers.append(player_obj)
            return True
        return False
    
    def add_bus_player(self, player_obj):
        if player_obj not in self.busPlayers:
            self.busPlayers.append(player_obj)
            return True
        return False
    
    def get_occupied_space(self):
        return len(self.carPlayers) * self.car_space + len(self.busPlayers) * self.bus_space
    
    def get_cars(self):
        return self.carPlayers
    
    def get_busPlayers(self):
        return self.busPlayers

    def get_players(self):
        return self.carPlayers + self.busPlayers