class Node:
    pass


class TileNode(Node):
    def __init__(self, resource: str, value: int):
        self.resource = resource
        self.value = value
        self.has_robber = False
        self.building_nodes = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.resource}{self.value}"


class BuildingNode(Node):
    def __init__(self, id):
        self.id = id
        self.building = 0  # is 0 == Nothing 1 == village, 2 == city
        self.player = None
        self.streets = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.building == 0:
            str_building = "None"
        elif self.building == 1:
            str_building = "Village"
        else:
            str_building = "City"
        return f"ID: {self.id} - {str_building}"
