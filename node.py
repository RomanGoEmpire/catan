class Node:
    pass


class TileNode(Node):
    def __init__(self, resource: str, value: int):
        self.resource = resource
        self.value = value
        self.has_robber = False
        self.building_nodes: list[BuildingNode] = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.resource}{self.value}"


class BuildingNode(Node):
    def __init__(self):
        self.building = 0  # is 0 == Nothing 1 == village, 2 == city
        self.streets: list[BuildingNode] = []
