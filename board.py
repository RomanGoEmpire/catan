from random import randint, shuffle
from node import TileNode

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


class Board:
    def __init__(self):
        self.tile_nodes = None
        self.building_nodes = None
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
        return board


if __name__ == "__main__":
    board = Board()
    print(board)
