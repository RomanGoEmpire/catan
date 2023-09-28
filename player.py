class Player:
    def __init__(self, name: str, color: str, position: int):
        # permanent
        self.name = name
        self.color = color
        self.position = position
        # bonus points
        self.has_longest_road = False
        self.has_army = False
        # pieces left
        self.village_tiles = 5
        self.cities_tiles = 4
        self.road_tiles = 15

        self.army = 0

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        pass

    def village_and_road(self, board):
        pass

    def place_village_and_road(self, board):
        pass

    def discard_cards(self):
        pass

    def rob(self, board, player):
        pass

    def select_tile_for_robber(self):
        pass

    def place_village(self, board):
        pass

    def place_city(self, board):
        pass

    def add(self, resources):
        pass

    def decision(self):
        pass

    def village_position(self, board):
        pass

    def city_position(self, board):
        pass

    def road_position(self, board):
        pass

    def play_card(self):
        pass

    def add_two_resources_because_of_action_card(self):
        pass

    def monopoly_resource(self):
        pass

    def remove(self, resource):
        pass

    def offer(self):
        pass
