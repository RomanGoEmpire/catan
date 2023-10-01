from random import randint, shuffle
from node import TileNode, BuildingNode

TOTAL_TILES = 18
RESOURCES = [
    "ore",
    "ore",
    "ore",
    "brick",
    "brick",
    "brick",
    "sheep",
    "sheep",
    "sheep",
    "sheep",
    "wood",
    "wood",
    "wood",
    "wood",
    "wheat",
    "wheat",
    "wheat",
    "wheat",
]
NUMBERS = [8, 4, 11, 12, 9, 10, 8, 3, 6, 2, 5, 10, 9, 4, 5, 6, 3, 11]

#     0   1   2
#   3   4   5   6
# 7   8   9   10  11
#   12  13  14  15
#     16  17  18

ADJACENCY_LIST = {
    0: [1, 3, 4],
    1: [0, 2, 4, 5],
    2: [1, 5, 6],
    3: [0, 4, 7, 8],
    4: [0, 1, 3, 5, 8, 9],
    5: [1, 2, 4, 6, 9, 10],
    6: [2, 5, 10, 11],
    7: [3, 8, 12],
    8: [3, 4, 7, 9, 12, 13],
    9: [4, 5, 8, 10, 13, 14],
    10: [5, 6, 9, 11, 14, 15],
    11: [6, 10, 15],
    12: [7, 8, 13, 16],
    13: [8, 9, 12, 14, 16, 17],
    14: [9, 10, 13, 15, 17, 18],
    15: [10, 11, 14, 18],
    16: [12, 13, 17],
    17: [13, 14, 16, 18],
    18: [14, 15, 17],
}
BUILDING_NODE_LIST = {
    0: [0, 1, 2, 3, 4, 5],
    1: [1, 2, 6, 7, 8, 9],
    2: [7, 8, 10, 11, 12, 13],
    3: [3, 4, 14, 15, 16, 17],
    4: [2, 3, 9, 14, 18, 19],
    5: [8, 9, 13, 18, 20, 21],
    6: [12, 13, 20, 22, 23, 24],
    7: [15, 16, 25, 26, 27, 28],
    8: [14, 15, 19, 25, 29, 30],
    9: [18, 19, 21, 29, 31, 32],
    10: [20, 21, 24, 31, 33, 34],
    11: [20, 23, 24, 33, 35, 36],
    12: [25, 26, 30, 38, 39, 40],
    13: [29, 30, 32, 38, 41, 42],
    14: [31, 32, 34, 41, 43, 44],
    15: [33, 34, 37, 43, 45, 46],
    16: [38, 39, 42, 47, 48, 49],
    17: [41, 42, 44, 47, 50, 51],
    18: [43, 44, 46, 50, 52, 53],
}


class Board:
    def __init__(self):
        self.building_nodes = [BuildingNode(id) for id in range(54)]
        self.board = self.generate_board()

    def __repr__(self):
        return str(self)

    def __str__(self):
        string = f"""
            {self.board[0]}  {self.board[1]} {self.board[2]}\n
          {self.board[3]} {self.board[4]} {self.board[5]} {self.board[6]}\n
        {self.board[7]} {self.board[8]} {self.board[9]} {self.board[10]} {self.board[11]}\n
          {self.board[12]} {self.board[13]} {self.board[14]} {self.board[15]}\n
            {self.board[16]}  {self.board[17]} {self.board[18]}\n
        """
        string = string.replace("ore", "🗻").replace("wheat", "🌾").replace("sheep", "🐑")
        string = (
            string.replace("brick", "🧱").replace("wood", "🌳").replace("desert", "🏜️")
        )
        return string

    def generate_board(self):
        resources = RESOURCES.copy()
        shuffle(resources)
        board = [None] * 19
        numbers = NUMBERS.copy()
        indexes = [0, 3, 7, 12, 16, 17, 18, 15, 11, 6, 2, 1, 5, 10, 14, 13, 8, 4, 9]
        desert_index = randint(0, 18)

        count = 0
        for i in indexes:
            if i == desert_index:
                board[i] = TileNode("desert", 0)
            else:
                board[i] = TileNode(resources.pop(), numbers[count])
                count += 1
            board[i].building_nodes = [
                self.building_nodes[i] for i in BUILDING_NODE_LIST[i]
            ]
        return board


if __name__ == "__main__":
    board = Board()
    print(board)
    print(board.building_nodes)
    for tile in board.board:
        print(tile.building_nodes)
    board.building_nodes[2].building = 1
    for tile in board.board:
        print(tile, tile.building_nodes)
