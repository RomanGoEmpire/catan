from player import Player


class Node:
    pass


class TileNode(Node):
    def __init__(self, value: int, resource: str):
        self.value = value
        self.resource = resource
        self.has_robber = False
        self.building_nodes: list[BuildingNode] = []


class BuildingNode(Node):
    def __init__(self):
        self.building = None  # is 0 | 1 | 2 --- 1 == village, 2 == city
        self.streets: list[BuildingNode] = []
