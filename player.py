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
        self.streets_tiles = 15

        self.army = 0
