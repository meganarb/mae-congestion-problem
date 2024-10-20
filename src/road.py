class Player:
    def __init__(self, id):
        self.id = id
        self.payoff = 0

    def get_id(self):
        return self.id
    
    def get_payoff(self):
        return self.payoff

class Car:
    def __init__(self):
        self.road_space = 1
        self.players = []

    def add_player(self, id):
        self.players.append(Player(id))

    def get_road_space(self):
        return self.road_space

    def get_players(self):
        return self.players

class Bus:
    def __init__(self):
        self.road_space = 2
        self.capacity = 5
        self.players = []

    def add_player(self, id):
        if len(self.players) < self.capacity:
            self.players.append(Player(id))
            return True
        else:
            return False

    def get_road_space(self):
        return self.road_space

    def get_capacity(self):
        return self.capacity    

    def get_players(self):
        return self.players

class Road:
    def __init__(self, space):
        self.space = space
        self.cars = []
        self.buses = []

    def add_car(self, id):
        car = Car()
        car.add_player(id)
        self.cars.append(car)

    def add_buses(self, id):
        if not self.buses:
            bus = Bus()
            bus.add_player(id)
            self.buses.append(bus)
        else:
            temp = self.buses[-1]
            if not temp.add_player(id):
                new_bus = Bus()
                new_bus.add_player(id)
                self.buses.append(new_bus)

    def get_buses(self):
        return self.buses
    
    def get_cars(self):
        return self.cars
    
    def get_space(self):
        return self.space
